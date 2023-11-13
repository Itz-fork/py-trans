# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/py-trans
# License: MIT License

import os, json, aiofiles

async def json_read():
    async with aiofiles.open(f"{os.path.dirname(__file__)}/data/languages.json", "r") as jsn_f:
        codes = json.load(jsn_f)
        return codes


# Get language code
def get_lang_code(name):
    with open(f"{os.path.dirname(__file__)}/data/languages.json", "r") as jsn_f:
        dt = json.load(jsn_f)
        return list(dt.keys())[list(dt.values()).index(str(name).lower())]

async def get_lang_code_async(name):
    async with aiofiles.open(f"{os.path.dirname(__file__)}/data/languages.json", "r") as jsn_f:
        dt = json.load(jsn_f)
        return list(dt.keys())[list(dt.values()).index(str(name).lower())]

# Get language name
def get_lang_name(code):
    with open(f"{os.path.dirname(__file__)}/data/languages.json", "r") as jsn_f:
        dt = json.load(jsn_f)
        return dt[str(code)]

async def get_lang_name_async(code):
    async with aiofiles.open(f"{os.path.dirname(__file__)}/data/languages.json", "r") as jsn_f:
        dt = json.load(jsn_f)
        return dt[str(name)]