import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='bankline-direct-parser',
    version='0.2',
    packages=[
        'bankline_parser', 'bankline_parser.data_services'
    ],
    include_package_data=True,
    license='BSD License',
    description='Parser for Bankline Direct banking information services',
    long_description=README,
    install_requires=[],
    classifiers=[
        'Intended Audience :: Python Developers',
    ],
    test_suite='tests',
)
