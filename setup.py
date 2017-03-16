import fnmatch
import os
import re

from setuptools import find_packages, setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

dir_path = os.path.dirname(os.path.realpath(__file__))

init_string = open(os.path.join(dir_path, 'mosfit', '__init__.py')).read()
VERS = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VERS, init_string, re.M)
__version__ = mo.group(1)
AUTH = r"^__author__ = ['\"]([^'\"]*)['\"]"
mo = re.search(AUTH, init_string, re.M)
__author__ = mo.group(1)
LICE = r"^__license__ = ['\"]([^'\"]*)['\"]"
mo = re.search(LICE, init_string, re.M)
__license__ = mo.group(1)

matches = []
for root, dirnames, filenames in os.walk('mosfit'):
    for filename in fnmatch.filter(filenames, '*.pyx'):
        matches.append(os.path.join(root, filename))


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


try:
    import pypandoc
    with open('README.md', 'r') as f:
        txt = f.read()
    txt = re.sub('<[^<]+>', '', txt)
    long_description = pypandoc.convert(txt, 'rst', 'md')
except ImportError:
    long_description = open('README.md').read()

setup(
    name='mosfit',
    packages=find_packages(),
    include_package_data=True,
    version=__version__,  # noqa
    description=('Maximum likelihood analysis for fitting '
                 'semi-analytical model predictions to observed '
                 'astronomical transient data.'),
    license=__license__,  # noqa
    author=__author__,  # noqa
    author_email='guillochon@gmail.com',
    install_requires=required,
    url='https://github.com/guillochon/mosfit',
    download_url=(
        'https://github.com/guillochon/mosfit/tarball/' + __version__),  # noqa
    keywords=['astronomy', 'fitting', 'monte carlo', 'modeling'],
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English', 'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics'
    ])
