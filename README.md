# py-trans
```py
from py_trans import PyTranslator

tr = PyTranslator()
print(tr.google("Hi", "es"))
```

<p align="center">
  A Fast, hassle-free way to translate text 📖
<p>

<p align="center">
  <kbd><a href="#features"><b>Features</b></a></kbd>
  <kbd><a href="#installation"><b>Install</b></a></kbd>
  <kbd><a href="#usage"><b>Usage</b></a></kbd>
</p>


## Features
- Simple and free
- Multiple translators to choose
- Both synchronous & asynchronous versions


## Supported translators
|                      Engine                      |   Function   |
| ------------------------------------------------ | --------------- |
|[Google Translate](https://translate.google.com/) | `google`        |
|[translate.com](https://www.translate.com/)       | `translate_com` |
|[MyMemory](https://mymemory.translated.net/)      | `my_memory`     |
|[Translate Dict](https://www.translatedict.com/)  | `translate_dict`     |


## Installation

```sh
pip3 install py-trans
```

<details>
  <summary><b>Install from source</b></summary>

  ```sh
  pip install git+https://github.com/Itz-fork/py-trans.git
  ```
</details>


## Usage

```py
# Sync version
from py_trans import PyTranslator

# Async version
from py_trans import Async_PyTranslator
```

- Detect language of the provided text
    - `detect`
    - 
        ```py
        tr.detect("Hello!")
        ```
- Translate text using Google translate
    - `google`
    - 
        ```py
        tr.google("Hello!", "es")
        ```
- Translate text using Translate.com
    - `translate_com`
    - 
        ```py
        tr.translate_com("Hello!", "es")
        ```
- Translate text using My Memory
    - `my_memory`
    - 
        ```py
        tr.my_memory("Hello!", "es")
        ```
- Translate text using Translate dict
    - `translate_dict`
    - 
        ```py
        tr.translate_dict("Hello!", "es")
        ```

> [!NOTE]
> All the above examples also applies to async version


## License
- Copyright (C) 2023 [@Itz-fork](https://github.com/Itz-fork)
- Licensed under [MIT](/LICENSE)