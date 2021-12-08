# Usage
Well, Usage of this module is very simple 😄. Follow below steps 👇,



### 1. Import py-trans in your python file

- **Sync version**
    ```python
    from py_trans import PyTranslator
    ```

- **Async version**
    ```python
    from py_trans import Async_PyTranslator
    ```


### 2. Now create an instance of py_trans.

- **Sync version**
    ```python
    py_t = PyTranslator()
    ```

- **Async version**
    ```python
    py_t = Async_PyTranslator()
    ```

If you need to choose the translation engine do something like this (For list of Supported Translation Engines please go to [this page](engines.md)),
```python
# For sync version
py_t = PyTranslator(provider="google")

# For async version
py_t = Async_PyTranslator(provider="google")
```


### 3. Let's translate

Now everything is done. So now you use this module 🤐.

> Recomended ⭐
>
> Take a look at [functions](functions.md) page for list of functions that are available in the py-trans library

For a example If you want to translate "`Hi, How are you?`" to "`Spanish`" do something like this,
```python
# es = Language code of spanish
print(py_t.translate("Hi, How are you?", "es"))
```


### Need more?

Can't find enough examples? Take a look at - [examples page](examples.md)
