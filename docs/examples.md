# Examples,

## Translation Example
Translate "`Hi`" to "`Spanish`" using "`google` translate engine. Output will return as a dict.

***Input***
```python
from py_trans import PyTranslator

py_t = PyTranslator(provider="google")

print(py_t.translate("Hi", "es"))
```
***Output***
```python
{'status': 'success', 'engine': 'google', 'translation': 'Hola', 'dest_lang': 'es', 'orgin_text': 'Hi', 'origin_lang': 'en'}
```

## Detect Source Language
For detecting source language you can use either normal translation mode or source language detection.

1. Using Translation Mode,
***Input***
```python
from py_trans import PyTranslator

py_t = PyTranslator(provider="google")

print(py_t.translate("Hi", "es")["origin_lang"])
```
***Output***
```python
en
```

2. Using Libre Language Detection Mode,
***Input***
```python
from py_trans import PyTranslator

py_t = PyTranslator(provider="google")

print(py_t._detect_lang("Hi"))
```
***Output***
```python
en
```
