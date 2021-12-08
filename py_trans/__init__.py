# Copyright (c) 2021 - Itz-fork
# Project: py_trans

import os
import json

# py-trans version
def get_pytrans_version():
    with open(f"{os.path.dirname(__file__)}/pytrans_data/version.json", "r") as jsn_f:
        ver = json.load(jsn_f)
        return ver["version"]
__version__ = get_pytrans_version()

from .translator import PyTranslator
from .async_translator import Async_PyTranslator