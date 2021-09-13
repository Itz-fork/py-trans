# Usage
Well, Usage of this module is very simple. For a example take a look at below code 👇,

```python
from py_trans import PyTranslator

# Create an instance of py_trans
# Choose Provider if you want, default one is google. (There are 4 providers for now)
x = PyTranslator(provider="google")

print(x.translate("Hi", "si"))
```

Above code will translate "Hi" into "Sinhala" and returns output as a dict.
