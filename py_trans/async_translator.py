# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/py-trans
# License: MIT License

from requests import exceptions, get
from aiohttp import ClientSession
from .errors import NoInternet, UnableToTranslate, UnknownError


class Async_PyTranslator:
    """
    Aync PyTranslator Class

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
                get("https://www.google.com/")
            except (exceptions.ConnectionError, exceptions.Timeout):
                raise NoInternet

    async def detect(self, text):
        """
        Detect language of the provided text

        Arguments:
            text: Text that needs to be detected
        """
        async with ClientSession() as client:
            async with client.post(
                "https://www.translate.com/translator/ajax_lang_auto_detect",
                data={"text_to_translate": str(text)},
            ) as fetch:
                resp = await fetch.json()
                if resp["result"] == "success":
                    return resp["language"]
                else:
                    raise UnknownError

    async def _fetch(self, url):
        async with ClientSession() as client:
            async with client.get(url) as ft:
                return await ft.json()

    async def google(self, text, dest):
        """
        Translate text using Google Translate

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
        """
        try:
            async with ClientSession() as client:
                async with client.get(
                    f"https://clients5.google.com/translate_a/t?client=at&sl=auto&tl={dest}&q={text}"
                ) as fetch:
                    resp = (await fetch.json())[0]
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

    async def translate_com(self, text, dest):
        """
        Translate text using translate.com

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
        """
        try:
            origin_lang = await self.detect(text)
            async with ClientSession() as client:
                async with client.post(
                    "https://www.translate.com/translator/ajax_translate",
                    data={
                        "text_to_translate": str(text),
                        "source_lang": origin_lang,
                        "translated_lang": dest,
                        "use_cache_only": "false",
                    },
                ) as fetch:
                    resp = await fetch.json()
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

    async def my_memory(self, text, dest):
        """
        Translate text using My Memory

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
        """
        try:
            origin_lang = self.detect(text)
            async with ClientSession() as client:
                async with client.get(
                    "https://api.mymemory.translated.net/get",
                    params={"q": text, "langpair": f"{origin_lang}|{dest}"},
                ) as fetch:
                    resp = await fetch.json()
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

    async def translate_dict(self, text, dest, detect_origin=False):
        """
        Translate text using Translate Dict

        Arguments:
            text: Text that needs to be translated
            dest: The language that the text needs to be translated into
            detect_origin: Pass "True" to detect origin language. Defaults to "False"
        """
        try:
            async with ClientSession() as client:
                async with client.get(
                    f"https://t3.translatedict.com/1.php?p1=auto&p2={dest}&p3={text}"
                ) as fetch:
                    resp = await fetch.text()
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
