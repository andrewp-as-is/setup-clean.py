<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-Unix-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/setup-clean.svg?maxAge=3600)](https://pypi.org/project/setup-clean/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/setup-clean.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/setup-clean.py/actions)

### Installation
```bash
$ [sudo] pip install setup-clean
```

#### Pros
+   super fast (shell)

#### Usage
```bash
$ usage: setup-clean path
```

#### Examples
```bash
$ setup-clean .
```

clean multiple repositories:
```bash
$ find . -type d -mindepth 1 -maxdepth 1 -exec setup-clean {} \;
```

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>