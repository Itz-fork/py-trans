# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/py-trans
# License: MIT License

# Version
import os, json


def get_version():
    with open(f"{os.path.dirname(__file__)}/data/version.json", "r") as jsn_f:
        ver = json.load(jsn_f)
        return ver["version"]


__version__ = get_version()


from .translator import PyTranslator
from .async_translator import Async_PyTranslator
from .extras import get_lang_code, get_lang_name
