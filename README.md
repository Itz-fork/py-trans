# py-trans
```python
from py_trans import PyTranslator

x = PyTranslator()
print(x.translate("Hi", "si"))
```

**py-trans**  is a Free Python library for translate text into different languages.

## Features
- Simple and Easy to use
- Synchronous & Asynchronous
- Different Translate Engines to choose

***Code less, translate more!***

## Supported Engines
For now py-trans supported for 5 translate engines (providers)
|                      Engine                      |   Engine Code   |
| ------------------------------------------------ | --------------- |
|[Google Translate](https://translate.google.com/) | `google`        |
|~~[LibreTranslate](https://libretranslate.com/)~~     | ~~`libre`~~         |
|[translate.com](https://www.translate.com/)       | `translate.com` |
|[MyMemory](https://mymemory.translated.net/)      | `my_memory`     |
|[Translate Dict](https://www.translatedict.com/)  | `translate_dict`     |

## Installation
**Install from pypi**

```
pip3 install py-trans
```
**Install from source**

If you want to try out latest features then install py-trans from the [source](https://github.com/Itz-fork/py-trans).
```
pip install git+https://github.com/Itz-fork/py-trans.git
```
If you want to check whether it's successfully installed or not just run the following command in your terminal. This will print out the current version of [py-trans](https://github.com/Itz-fork/py-trans). So you can use this to check the version also.
```bash
echo 'from py_trans import __version__ as v; print(v)' | python3
```

## Docs
> "Stop it, Get some help"
>
If you want more information about usage of thsi module or need some examples to get started, just read the docs of py-trans - [Click here](https://itz-fork.github.io/py-trans/)

## License & Copyright
- **[py-trans](https://github.com/Itz-fork/py-trans) is licensed under [MIT License](https://github.com/Itz-fork/py-trans/blob/main/LICENSE)**

- **Copyright (c) 2021 Itz-fork**
