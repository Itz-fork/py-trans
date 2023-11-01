# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/py-trans
# License: MIT License

import os, json, aiofiles

from sys import _getframe
from functools import wraps
from inspect import signature


# Taken from https://github.com/dabeaz/curio/blob/master/curio/meta.py
def from_coroutine(level=2, _cache={}):
    f_code = _getframe(level).f_code
    if f_code in _cache:
        return _cache[f_code]
    if f_code.co_flags & _CO_FROM_COROUTINE:
        _cache[f_code] = True
        return True
    else:
        if (f_code.co_flags & _CO_NESTED and f_code.co_name[0] == '<'):
            return from_coroutine(level + 2)
        else:
            _cache[f_code] = False
            return False

def awaitable(syncfunc):
    def decorate(asyncfunc):
        if signature(syncfunc) != signature(asyncfunc):
            raise TypeError(f'{syncfunc.__name__} and async {asyncfunc.__name__} have different signatures')

        @wraps(asyncfunc)
        def wrapper(*args, **kwargs):
            if from_coroutine():
                return asyncfunc(*args, **kwargs)
            else:
                return syncfunc(*args, **kwargs)
        wrapper._syncfunc = syncfunc
        wrapper._asyncfunc = asyncfunc
        wrapper._awaitable = True
        wrapper.__doc__ = syncfunc.__doc__ or asyncfunc.__doc__
        return wrapper
    return decorate


# Read json file
def json_read():
    with open(f"{os.path.dirname(__file__)}/data/languages.json", "r") as jsn_f:
        codes = json.load(jsn_f)
        return codes

@awaitable(json_read)
async def json_read():
    async with aiofiles.open(f"{os.path.dirname(__file__)}/data/languages.json", "r") as jsn_f:
        codes = json.load(jsn_f)
        return codes


# Get language code
def get_lang_code(name):
    dt = json_read()
    return list(dt.keys())[list(dt.values()).index(str(name).lower())]

@awaitable(get_lang_code)
async def get_lang_code(name):
    dt = await json_read()
    return list(dt.keys())[list(dt.values()).index(str(name).lower())]

# Get language name
def get_lang_name(code):
    dt = json_read()
    return dt[str(code)]

@awaitable(get_lang_name)
async def get_lang_name(code):
    dt = await json_read()
    return dt[str(name)]