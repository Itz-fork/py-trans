# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/py-trans
# License: MIT License


class NoInternet(Exception):
    "Please turn on your internet connection!"
    pass

class UnableToTranslate(Exception):
    def __init__(self, e):
        super().__init__({"status": "failed", "error": e})

class UnknownError(Exception):
    "Unknown error"
    pass