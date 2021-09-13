# py-trans
Free Python library for translate text into different languages.

## Supported Engines
For now py-trans supported for four translate engines (providers)
- [Google Translate](https://translate.google.com/) - "google"
- [LibreTranslate](https://libretranslate.com/) - "libre"
- [translate.com](https://www.translate.com/) - "translate.com"
- [MyMemory](https://mymemory.translated.net/) - "my_memory"

## Installation
**Install from pypi**
```
pip3 install py-trans
```
**Install from source**
```
pip install git+https://github.com/Itz-fork/py-trans.git
```

## Usage
Example code snippet to use py-trans

```python
from py_trans import PyTranslator

# Create an instance of py_trans
# Choose Provider if you want, default one is google. (There are 4 providers for now)
x = PyTranslator(provider="google")

print(x.translate("Hi", "si"))
```

## Docs
Here is the [Documentation](https://itz-fork.github.io/py-trans/) of py-trans
