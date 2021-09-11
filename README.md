# py-trans
Free Python library for translate text into different languages.

## Supported Engines
For now py-trans supported for two translate engines (providers)
- [Google Translate](https://translate.google.com/) - "google"
- [LibreTranslate](https://libretranslate.com/) - "libre"

## Installation
**Install from source**
```
pip install git+https://github.com/Itz-fork/py-trans.git
```

## Usage
Some example code snippet to use py-trans

```python
from py_trans import PyTranslator

# Create an instance of py_trans
x = PyTranslator(provider="google")

print(x.translate("Hi", "si"))
```

## Docs
For now there is no documentation, but still you can get some help using Docstrings. Use below code for it.
```python
from py_trans import PyTranslator

print(help(PyTranslator.translate))
```
