# Project: py-trans
# Author: Itz-fork

import requests

class NoInternetConnection(Exception):
    pass

class UnknownErrorOccurred(Exception):
    pass

def check_internet_connection():
    try:
        requests.get("https://www.google.com/")
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        raise NoInternetConnection("Your device hasn't connected to internet yet! Please turn on the internet connection to keep using py-trans library!")