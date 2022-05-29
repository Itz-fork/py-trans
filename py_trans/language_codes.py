# Project: py-trans
# Author: itz-fork

# List of language codes (ISO 639-1). Thanks to mathguide
LANGUAGE_CODES = {
    "aa": "Afar",
    "ab": "Abkhazian",
    "af": "Afrikaans",
    "am": "Amharic",
    "ar": "Arabic",
    "as": "Assamese",
    "ay": "Aymara",
    "az": "Azerbaijani",
    "ba": "Bashkir",
    "be": "Byelorussian",
    "bg": "Bulgarian",
    "bh": "Bihari",
    "bi": "Bislama",
    "bn": "Bengali",
    "bo": "Tibetan",
    "br": "Breton",
    "ca": "Catalan",
    "co": "Corsican",
    "cs": "Czech",
    "cy": "Welch",
    "da": "Danish",
    "de": "German",
    "dz": "Bhutani",
    "el": "Greek",
    "en": "English",
    "eo": "Esperanto",
    "es": "Spanish",
    "et": "Estonian",
    "eu": "Basque",
    "fa": "Persian",
    "fi": "Finnish",
    "fj": "Fiji",
    "fo": "Faeroese",
    "fr": "French",
    "fy": "Frisian",
    "ga": "Irish",
    "gd": "Scots Gaelic",
    "gl": "Galician",
    "gn": "Guarani",
    "gu": "Gujarati",
    "ha": "Hausa",
    "hi": "Hindi",
    "he": "Hebrew",
    "hr": "Croatian",
    "hu": "Hungarian",
    "hy": "Armenian",
    "ia": "Interlingua",
    "id": "Indonesian",
    "ie": "Interlingue",
    "ik": "Inupiak",
    "in": "Indonesian",
    "is": "Icelandic",
    "it": "Italian",
    "iu": "Inuktitut",
    "iw": "Hebrew",
    "ja": "Japanese",
    "ji": "Yiddish",
    "jw": "Javanese",
    "ka": "Georgian",
    "kk": "Kazakh",
    "kl": "Greenlandic",
    "km": "Cambodian",
    "kn": "Kannada",
    "ko": "Korean",
    "ks": "Kashmiri",
    "ku": "Kurdish",
    "ky": "Kirghiz",
    "la": "Latin",
    "ln": "Lingala",
    "lo": "Laothian",
    "lt": "Lithuanian",
    "lv": "Latvian",
    "mg": "Malagasy",
    "mi": "Maori",
    "mk": "Macedonian",
    "ml": "Malayalam",
    "mn": "Mongolian",
    "mo": "Moldavian",
    "mr": "Marathi",
    "ms": "Malay",
    "mt": "Maltese",
    "my": "Burmese",
    "na": "Nauru",
    "ne": "Nepali",
    "ni": "Dutch",
    "no": "Norwegian",
    "oc": "Occitan",
    "om": "Oromo",
    "or": "Oriya",
    "pa": "Punjabi",
    "pl": "Polish",
    "ps": "Pashto",
    "pt": "Portuguese",
    "qu": "Quechua",
    "rm": "Rhaeto-Romance",
    "rn": "Kirundi",
    "ro": "Romanian",
    "ru": "Russian",
    "rw": "Kinyarwanda",
    "sa": "Sanskrit",
    "sd": "Sindhi",
    "sg": "Sangro",
    "sh": "Serbo-Croatian",
    "si": "Sinhala",
    "sk": "Slovak",
    "sl": "Slovenian",
    "sm": "Samoan",
    "sn": "Shona",
    "so": "Somali",
    "sq": "Albanian",
    "sr": "Serbian",
    "ss": "Siswati",
    "st": "Sesotho",
    "su": "Sudanese",
    "sv": "Swedish",
    "sw": "Swahili",
    "ta": "Tamil",
    "te": "Tegulu",
    "tg": "Tajik",
    "th": "Thai",
    "ti": "Tigrinya",
    "tk": "Turkmen",
    "tl": "Tagalog",
    "tn": "Setswana",
    "to": "Tonga",
    "tr": "Turkish",
    "ts": "Tsonga",
    "tt": "Tatar",
    "tw": "Twi",
    "ug": "Uigur",
    "uk": "Ukrainian",
    "ur": "Urdu",
    "uz": "Uzbek",
    "vi": "Vietnamese",
    "vo": "Volapuk",
    "wo": "Wolof",
    "xh": "Xhosa",
    "yi": "Yiddish",
    "yo": "Yoruba",
    "za": "Zhuang",
    "zh": "Chinese",
    "zu": "Zulu"
}


def _get_full_lang_name(text):
    try:
        lang_name = LANGUAGE_CODES.get(text)
        return f"{lang_name} ({text})"
    except:
        return "Language Not Found!"


def _get_lang_code(text):
    try:
        lang_code = list(LANGUAGE_CODES.keys())[
            list(LANGUAGE_CODES.values()).index(text)]
        return f"{lang_code} ({text})"
    except:
        return "Language Not Found!"
