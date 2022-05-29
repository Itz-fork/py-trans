# Project: py-trans
# Author: Itz-fork
from aiohttp import ClientSession
from .language_codes import _get_full_lang_name, _get_lang_code
from .errors import check_internet_connection, UnknownErrorOccurred, DeprecatedMethod


class Async_PyTranslator:
    """
    Async PyTranslator Class


    ## Providers:

        google - Google Translate
        libre - LibreTranslate Engine
        translate.com - translate.com Translate
        my_memory - MyMemory Translate
        translate_dict - Translate Dict

    ## Arguments:

        provider - Provider of Translator. (Must be a supported provider)
    """

    def __init__(self, provider="google"):
        # Checking internet connection
        check_internet_connection()
        self.providers = ["google", "libre",
                          "translate.com", "my_memory", "translate_dict"]
        if provider in self.providers:
            self.provider = provider
        # Headers
        self.lheader = {"Origin": "https://libretranslate.com",
                        "Host": "libretranslate.com", "Referer": "https://libretranslate.com/"}

    async def translate(self, text, dest_lang="en"):
        """
        Translator Function

        Argument(s):
            text - Source Text (Text that need to be translated)
            dest_lang - Destination Language

        Example(s):
            await async_pytranslator.translate(text="Hi, How are you?", dest_lang="si")
        """
        if self.provider == "google":
            return await self.google_translate(text, dest_lang)
        elif self.provider == "libre":
            raise DeprecatedMethod(
                "Libre is no longer supported as it's translation accuracy is low")
            # return await self.libre_translate(text, dest_lang)
        elif self.provider == "translate.com":
            return await self.translate_com(text, dest_lang)
        elif self.provider == "my_memory":
            return await self.my_memory(text, dest_lang)
        elif self.provider == "translate_dict":
            return await self.translate_dict(text, dest_lang)
        else:
            return

    # Google Translate
    async def google_translate(self, text, dest_lang):
        r_url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={dest_lang}&q={text}"
        try:
            async with ClientSession() as tr_ses:
                async with tr_ses.get(r_url) as get_req:
                    resp = (await get_req.json())[0]
                    translation = resp[0]
                    origin_text = text
                    origin_lang = await self.get_lang_name(resp[1])
                    dest_lang_f = await self.get_lang_name(dest_lang)
                    tr_dict = {"status": "success", "engine": "Google Translate", "translation": translation,
                               "dest_lang": dest_lang_f, "orgin_text": origin_text, "origin_lang": origin_lang}
                    return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}

    # LibreTranslate
    async def _detect_lang(self, text, full_name=False):
        r_url = "https://libretranslate.com/detect"
        ld_data = {"q": str(text)}
        try:
            async with ClientSession() as tr_ses:
                async with tr_ses.post(r_url, data=ld_data) as get_req:
                    request_resp = await get_req.json()
                    language_code = request_resp[0]["language"]
        except:
            # If can't detect the language let's think it's just english (RIP moment)
            language_code = "en"
        if full_name is False:
            return language_code
        else:
            return await self.get_lang_name(language_code)

    async def libre_translate(self, text, dest_lang):
        r_url = "https://libretranslate.com/translate"
        try:
            source_lang = await self._detect_lang(text=text, full_name=False)
            l_data = {"q": str(text), "source": source_lang,
                      "target": dest_lang}
            async with ClientSession() as tr_ses:
                async with tr_ses.post(r_url, data=l_data) as get_req:
                    request_resp = await get_req.json()
                    translation = request_resp["translatedText"]
                    origin_lang = await self.get_lang_name(source_lang)
                    dest_lang_f = await self.get_lang_name(dest_lang)
                    tr_dict = {"status": "success", "engine": "LibreTranslate", "translation": translation,
                               "dest_lang": dest_lang_f, "orgin_text": str(text), "origin_lang": origin_lang}
                    return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}

    # Translate.com
    async def translate_com(self, text, dest_lang):
        r_url = "https://www.translate.com/translator/ajax_translate"
        try:
            source_lang = await self._detect_lang(text=text, full_name=False)
            tr_data = {"text_to_translate": str(
                text), "source_lang": source_lang, "translated_lang": dest_lang, "use_cache_only": "false"}
            async with ClientSession() as tr_ses:
                async with tr_ses.post(url=r_url, data=tr_data) as get_req:
                    request_resp = await get_req.json(content_type='text/html')
                    translation = request_resp["translated_text"]
                    origin_lang = await self.get_lang_name(text)
                    dest_lang_f = await self.get_lang_name(dest_lang)
                    tr_dict = {"status": "success", "engine": "Translate.com", "translation": translation,
                               "dest_lang": dest_lang_f, "orgin_text": origin_lang, "origin_lang": origin_lang}
                    return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}

    # My Memory
    async def my_memory(self, text, dest_lang):
        r_url = "https://api.mymemory.translated.net/get"
        try:
            source_lang = await self._detect_lang(text=text, full_name=False)
            m_params = {"q": text, "langpair": f"{source_lang}|{dest_lang}"}
            async with ClientSession() as tr_ses:
                async with tr_ses.get(r_url, params=m_params) as get_req:
                    request_resp = await get_req.json()
                    translation = request_resp["matches"][0]["translation"]
                    origin_lang = await self.get_lang_name(source_lang)
                    dest_lang_f = await self.get_lang_name(dest_lang)
                    tr_dict = {"status": "success", "engine": "MyMemory", "translation": translation,
                               "dest_lang": dest_lang_f, "orgin_text": str(text), "origin_lang": origin_lang}
                    return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}

    # Translate Dict
    async def translate_dict(self, text, dest_lang):
        r_url = f"https://t3.translatedict.com/1.php?p1=auto&p2={dest_lang}&p3={text}"
        try:
            async with ClientSession() as tr_ses:
                async with tr_ses.get(r_url) as get_req:
                    request_resp = await get_req.text()
                    origin_lang = await self._detect_lang(text=text, full_name=True)
                    dest_lang_f = await self.get_lang_name(dest_lang)
                    tr_dict = {"status": "success", "engine": "Translate Dict", "translation": request_resp,
                               "dest_lang": dest_lang_f, "orgin_text": str(text), "origin_lang": origin_lang}
                    return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}

    # Get Language Names
    async def get_lang_name(self, text):
        if len(text) == 2:
            return _get_full_lang_name(text)
        else:
            if len(text) <= 3:
                return "Not a full language name"
            else:
                return _get_lang_code(text)
