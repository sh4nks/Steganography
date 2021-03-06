#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

with open("README.md") as readme_file:
    readme = readme_file.read()

requirements = ["Pillow>=5.3.0", "numpy>=1.15.4", "Click>=7.0"]


setup(
    author="Ryan Gibson",
    author_email="ryanalexandergibson@gmail.com",
    name="stego_lsb",
    version="0.1.0",
    description="stego lsb",
    keywords="stego lsb",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/ragibson/Steganography",
    install_requires=requirements,
    entry_points="""
        [console_scripts]
        stegolsb=stego_lsb.cli:main
    """,
    include_package_data=True,
    packages=find_packages(include=["stego_lsb"]),
    zip_safe=False,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
