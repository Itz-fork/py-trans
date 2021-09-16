# Functions
List of functions that are available on py-trans

## Translate (`translate`)
This function is used for translating text using different translation engines ([List of supported engines](engines.md)). </br>
**Arguments,**
  - `text` - The text that need to be translated
  - `dest_lang` - Language code into which the `text` need to be translated

Output will return as a dict. </br>
Example: [Click here](examples.md#translation-example)


## Detect Source language (`_detect_lang`)
This function is used for detecting source language of the given text using Libre language detection.
**Arguments,**
  - `text` - The text that need to get source language

Output will return as a string. </br>
Example: [Click here](examples.md#detect-source-language)


## Get Language Name (`get_lang_name`)
Using this function you can get **Full language name by it's [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code** or **[ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) language code by it'ls full name**. There are over 140+ language codes for now.
**Arguments,**
  - `text` - If you want to get **Full language name** then pass the language code. else if you need to get **Language code** then pass full language name. For the language list [Click here](https://github.com/Itz-fork/py-trans/blob/main/py_trans/language_codes.py#L5-L148)
  - `full_name` - Set this to `True` if you need full form ablong-side with language code. Defaults to `False`

Output will return as a string. </br>
Example: [Click here](examples.md#get-language-name)
