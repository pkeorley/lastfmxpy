# Copyright © 2023 pkeorley
#
# This source code is licensed under the MIT license found in the LICENSE
# file in the root directory of this source tree.

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='lastfmxpy',
    version='1.0.2',
    python_requires='>=3.10',
    install_requires=['requests>=2.31.0'],
    packages=find_packages(exclude=['.venv']),
    url='https://github.com/pkeorley/lastfmxpy',
    license='MIT',
    licence_files=['LICENSE'],
    author='pkeorley',
    author_email='pkeorley@gmail.com',
    description='A tool that helps to work effectively with the API from last.fm',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
