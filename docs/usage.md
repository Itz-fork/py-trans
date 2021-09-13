# Usage
Well, Usage of this module is very simple 😄. Follow below steps 👇,

**1. Import py-trans in your python file**
```python
from py_trans import PyTranslator
```

**2. Now create an instance of py_trans.**
```python
py_t = PyTranslator()
```
If you need to choose the translation engine do something like this (For list of Supported Translation Engines please go to [this page](engines.md)),
```python
py_t = PyTranslator(provider="google")
```

**3. Let's translate**
Now everything is done. So now you use this module 🤐. For a example If you want to translate "`Hi`" to "`Spanish`" do something like this,
```python
# es = Language code of spanish
print(x.translate("Hi", "es"))
```
