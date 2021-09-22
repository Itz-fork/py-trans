# Project: py-trans
# Author: Itz-fork
import requests
from .language_codes import _get_full_lang_name, _get_lang_code

class PyTranslator:
    """
    PyTranslator Class

    Note:
        Before Trying to Translate Create an instance of this with provider (Default provider is google)
    
    Providers:
        google - Google Translate
        libre - LibreTranslate Engine
        translate.com - translate.com Translate
        my_memory - MyMemory Translate
        translate_dict - Translate Dict

    Argument(s):
        provider - Provider of Translator. (Must be a supported provider)
    
    Example(s):
        pytranslator = PyTranslator(provider="google")
    """
    def __init__(self, provider="google"):
        self.providers = ["google", "libre", "translate.com", "my_memory", "translate_dict"]
        if provider in self.providers:
            self.provider = provider
        else:
            self.provider = "google"
        # Headers
        self.gheader = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        self.lheader = {"Origin": "https://libretranslate.com", "Host": "libretranslate.com", "Referer": "https://libretranslate.com/"}


    def translate(self, text, dest_lang="en"):
        """
        Translator Function

        Argument(s):
            text - Source Text (Text that need to be translated)
            dest_lang - Destination Language
        
        Example(s):
            pytranslator.translate(text="Hi, How are you?", dest_lang="si")
        """
        if self.provider == "google":
            return self.google_translate(text, dest_lang)
        elif self.provider == "libre":
            return self.libre_translate(text, dest_lang)
        elif self.provider == "translate.com":
            return self.translate_com(text, dest_lang)
        elif self.provider == "my_memory":
            return self.my_memory(text, dest_lang)
        elif self.provider == "translate_dict":
            return self.translate_dict(text, dest_lang)
        else:
            return
    
    # Google Translate
    def google_translate(self, text, dest_lang):
        r_url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={dest_lang}&q={text}"
        try:
            request_resp = requests.get(r_url, headers=self.gheader).json()
            translation = request_resp['sentences'][0]['trans']
            origin_text = request_resp['sentences'][0]['orig']
            origin_lang = self.get_lang_name(request_resp['src'])
            dest_lang_f = self.get_lang_name(dest_lang)
            tr_dict = {"status": "success", "engine": "Google Translate", "translation": translation, "dest_lang": dest_lang_f, "orgin_text": origin_text, "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # LibreTranslate
    def _detect_lang(self, text, full_name=False):
        try:
            r_url = requests.post("https://libretranslate.com/detect", data={"q": str(text)}, headers=self.lheader).json()
            language_code = r_url[0]["language"]
        except:
            # If can't detect the language let's think it's just english (RIP moment)
            language_code = "en"
        if full_name is False:
            return language_code
        else:
            return self.get_lang_name(language_code)
    
    def libre_translate(self, text, dest_lang):
        try:
            source_lang = self._detect_lang(text=text, full_name=False)
            r_url = requests.post("https://libretranslate.com/translate", data={"q": str(text), "source": source_lang, "target": dest_lang}, headers=self.lheader).json()
            translation = r_url["translatedText"]
            origin_lang = self.get_lang_name(source_lang)
            dest_lang_f = self.get_lang_name(dest_lang)
            tr_dict = {"status": "success", "engine": "LibreTranslate", "translation": translation, "dest_lang": dest_lang_f, "orgin_text": str(text), "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # Translate.com
    def translate_com(self, text, dest_lang):
        try:
            source_lang = self._detect_lang(text=text, full_name=False)
            r_url = requests.post(url="https://www.translate.com/translator/ajax_translate", data={"text_to_translate": str(text), "source_lang": source_lang, "translated_lang": dest_lang, "use_cache_only": "false"}).json()
            translation = r_url["translated_text"]
            origin_lang = self.get_lang_name(source_lang)
            dest_lang_f = self.get_lang_name(dest_lang)
            tr_dict = {"status": "success", "engine": "Translate.com", "translation": translation, "dest_lang": dest_lang_f, "orgin_text": origin_lang, "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # My Memory
    def my_memory(self, text, dest_lang):
        try:
            source_lang = self._detect_lang(text=text, full_name=False)
            r_url = requests.get("https://api.mymemory.translated.net/get", params={"q": text, "langpair": f"{source_lang}|{dest_lang}"}).json()
            translation = r_url["matches"][0]["translation"]
            origin_lang = self.get_lang_name(source_lang)
            dest_lang_f = self.get_lang_name(dest_lang)
            tr_dict = {"status": "success", "engine": "MyMemory", "translation": translation, "dest_lang": dest_lang_f, "orgin_text": str(text), "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # Translate Dict
    def translate_dict(self, text, dest_lang):
        try:
            r_url = requests.get(f"https://t3.translatedict.com/1.php?p1=auto&p2={dest_lang}&p3={text}").text
            origin_lang = self._detect_lang(text=text, full_name=True)
            dest_lang_f = self.get_lang_name(dest_lang)
            tr_dict = {"status": "success", "engine": "Translate Dict", "translation": r_url, "dest_lang": dest_lang_f, "orgin_text": str(text), "origin_lang": origin_lang}
            return tr_dict
        except Exception as e:
            return {"status": "failed", "error": e}
    
    # Get Language Names
    def get_lang_name(self, text):
        if len(text) == 2:
            return _get_full_lang_name(text)
        else:
            if len(text) <= 3:
                return "Not a full language name"
            else:
                return _get_lang_code(text)