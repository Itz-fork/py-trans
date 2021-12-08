# Examples,

Some code snippets to use [py-trans](https://github.com/Itz-fork/py-trans)

> Note ⚠️
>
> In these examples we're using sync version. However async version is also the same. To know more take a look at [usage page](usage.md) for more info on it!



## Translation Example

**Function:** [translate](functions.md#translate-translate) </br>
**What example does?:** Translate "`Hi`" to "`Spanish`" using "`google` translate engine.

***Input***
```python
from py_trans import PyTranslator

py_t = PyTranslator(provider="google")

print(py_t.translate("Hi", "es"))
```
***Output***
```python
{'status': 'success', 'engine': 'google', 'translation': 'Hola', 'dest_lang': 'Spanish (es)', 'orgin_text': 'Hi', 'origin_lang': 'English (en)'}
```


## Detect Source Language

**Function:** [_detect_lang_](functions.md#detect-source-language-_detect_lang) </br>
**What example does?:** Detecting source language using normal translation mode(1) and using libre language detect(2)

   1. Using Translation Mode,
***Input***
```python
from py_trans import PyTranslator

py_t = PyTranslator(provider="google")

print(py_t.translate("Hi", "es")["origin_lang"])
```
***Output***
```python
English (en)
```

   2. Using Libre Language Detection Mode,
***Input***
```python
from py_trans import PyTranslator

py_t = PyTranslator(provider="libre")

print(py_t._detect_lang("Hi"))
```
***Output***
```python
en
```


## Get Language Name

**Function:** [get_language_name](functions.md#get-language-name-get_lang_name) </br>
**What example does?:** Get full language name of language code `si`

***Input***
```python
from py_trans import PyTranslator

py_t = PyTranslator()

print(py_t.get_lang_name("si"))
```
***Output***
```python
Sinhala (si)
```
