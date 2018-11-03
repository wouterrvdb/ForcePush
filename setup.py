# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ForcePush',
    version='0.1.0',
    description='ForcePush',
    long_description=readme,
    author='wouterrvdb, Autom3',
    # author_email='',
    url='https://github.com/wouterrvdb/ForcePush',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)