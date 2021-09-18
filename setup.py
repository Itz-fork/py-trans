# Copyright (c) 2021 - Itz-fork
# Project: py-trans
import os
from setuptools import setup, find_packages
from py_trans import __version__ as pyt_version

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

if os.path.isfile('requirements.txt'):
  with open('requirements.txt') as req:
    reques = req.read().splitlines()
else:
  reques = [
    'requests'
  ]

if os.path.isfile('README.md'):
  with open(('README.md'), encoding='utf-8') as readmeh:
    big_description = readmeh.read()
else:
  big_description = "py_trans is a free python library to translate text to different languages."


setup(name='py-trans',
version=pyt_version,
description='Free python library to translate text to different languages.',
url='https://github.com/Itz-fork/py-trans',
author='Itz-fork',
author_email='itz-fork@users.noreply.github.com',
license='MIT',
packages=find_packages(),
download_url=f"https://github.com/Itz-fork/py-trans/releases/tag/py-trans-pypi-{pyt_version}",
keywords=['python', 'translator', 'py-trans'],
long_description=big_description,
long_description_content_type='text/markdown',
install_requires=reques,
classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.9',
  ],
)
