# Supported Engines
For now py-trans supported for four translate engines (providers)


|                      Engine                      |   Engine Code   |
| ------------------------------------------------ | --------------- |
|[Google Translate](https://translate.google.com/) | `google`        |
|[LibreTranslate](https://libretranslate.com/)     | `libre`         |
|[translate.com](https://www.translate.com/)       | `translate.com` |
|[MyMemory](https://mymemory.translated.net/)      | `my_memory`     |


**Use `Engine Code` to choose Translation Engine while creating instance of py_trans.**
Ex:-
```python
py_t = PyTranslator(provider="google")
```
