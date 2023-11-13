# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/py-trans
# License: MIT License

import os, json
from setuptools import setup, find_packages


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

# Readme & Reqs
if os.path.isfile("requirements.txt"):
    reques = [r.strip() for r in open("requirements.txt").readlines()]
else:
    reques = ["requests", "aiohttp"]

if os.path.isfile("README.md"):
    with open(("README.md"), encoding="utf-8") as readmeh:
        lg_desc = readmeh.read()
else:
    lg_desc = "py-trans is a free python library to translate text into different languages."


# py-trans version
def get_pytrans_version():
    with open("py_trans/data/version.json", "r") as jsn_f:
        ver = json.load(jsn_f)
        return ver["version"]

pyt_version = get_pytrans_version()


setup(name="py-trans",
      version=pyt_version,
      description="Free python library to translate text to different languages.",
      url="https://github.com/Itz-fork/py-trans",
      author="Itz-fork",
      author_email="git.itzfork@gmail.com",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      download_url=f"https://github.com/Itz-fork/py-trans/releases/tag/py-trans-pypi-{pyt_version}",
      keywords=["google translate", "text translator", "translator", "py-trans"],
      long_description=lg_desc,
      long_description_content_type="text/markdown",
      install_requires=reques,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "Topic :: Education",
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.9",
          "Programming Language :: Python :: 3.10",
          "Programming Language :: Python :: 3.11",
      ],
      )