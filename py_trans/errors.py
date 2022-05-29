# Project: py-trans
# Author: Itz-fork

from requests import get, exceptions


class NoInternetConnection(Exception):
    pass


class UnknownErrorOccurred(Exception):
    pass


class DeprecatedMethod(Exception):
    pass


def check_internet_connection():
    try:
        get("https://www.google.com/")
    except (exceptions.ConnectionError, exceptions.Timeout):
        raise NoInternetConnection(
            "Your device hasn't connected to internet yet! Please turn on the internet connection to keep using py-trans library!")
