# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/py-trans
# License: MIT License

import requests
from .errors import NoInternet, UnableToTranslate, UnknownError


class PyTranslator:
    """
    PyTranslator Class

    Methods:

        detect: Detect language of the provided text
        google: Translate text using Google Translate
        translate_com: Translate text using Translate.com
        my_memory: Translate text using My Memory
        translate_dict: Translate text using Translate Dict
    """

    def __init__(self, connection_check=True):
        # Check internet connection
        if connection_check is True:
            try:
                requests.get("https://www.google.com/")
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
                raise NoInternet

    def detect(self, text):
        """
        Detect language of the provided text

        Arguments:
            text: Text that needs to be detected
        """
        resp = requests.post(
            "https://www.translate.com/translator/ajax_lang_auto_detect",
            data={"text_to_translate": str(text)},
        ).json()
        if resp["result"] == "success":
            return resp["language"]
        else:
            raise UnknownError

    def google(self, text, dest):
        """
        Translate text using Google Translate

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
        """
        try:
            resp = requests.get(
                f"https://clients5.google.com/translate_a/t?client=at&sl=auto&tl={dest}&q={text}"
            ).json()[0]
            out = {
                "status": "success",
                "engine": "Google Translate",
                "translation": resp[0],
                "dest": dest,
                "orgin": text,
                "origin_lang": resp[1],
            }
            return out
        except Exception as e:
            raise UnableToTranslate(e)

    def translate_com(self, text, dest):
        """
        Translate text using translate.com

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
        """
        try:
            origin_lang = self.detect(text)
            resp = requests.post(
                "https://www.translate.com/translator/ajax_translate",
                data={
                    "text_to_translate": str(text),
                    "source_lang": origin_lang,
                    "translated_lang": dest,
                    "use_cache_only": "false",
                },
            ).json()
            out = {
                "status": "success",
                "engine": "Translate.com",
                "translation": resp["translated_text"],
                "dest": dest,
                "orgin": text,
                "origin_lang": origin_lang,
            }
            return out
        except Exception as e:
            raise UnableToTranslate(e)

    def my_memory(self, text, dest):
        """
        Translate text using My Memory

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
        """
        try:
            origin_lang = self.detect(text)
            resp = requests.get(
                "https://api.mymemory.translated.net/get",
                params={"q": text, "langpair": f"{origin_lang}|{dest}"},
            ).json()
            out = {
                "status": "success",
                "engine": "My Memory",
                "translation": resp["matches"][0]["translation"],
                "dest": dest,
                "orgin": text,
                "origin_lang": origin_lang,
            }
            return out
        except Exception as e:
            raise UnableToTranslate(e)

    def translate_dict(self, text, dest, detect_origin=False):
        """
        Translate text using Translate Dict

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
            detect_origin: Pass "True" to detect origin language. Defaults to "False"
        """
        try:
            resp = requests.get(
                f"https://t3.translatedict.com/1.php?p1=auto&p2={dest}&p3={text}"
            ).text
            if detect_origin is True:
                origin_lang = self.detect(text)
            else:
                origin_lang = None
            out = {
                "status": "success",
                "engine": "Translate Dict",
                "translation": resp,
                "dest": dest,
                "orgin": text,
                "origin_lang": origin_lang,
            }
            return out
        except Exception as e:
            return UnableToTranslate(e)
