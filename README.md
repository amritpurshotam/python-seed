# python-seed

Seed project implementing Python best practices with setup instructions. This is mainly for VS Code users.

## Virtual Environment

### Installation
```
py -3.6 -m venv env
.\env\Scripts\activate
python -m pip install --upgrade pip
```

### Configure VS Code

1. Open Settings with `Ctrl+,` and navigate to the Workspace tab.
2. Search `python.pythonPath`
3. Set it to `.\env\Scripts\python.exe`

## Formatter

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Formatting makes code easier to read by human beings by applying specific rules and conventions for line spacing, indents, spacing around operators, and so on. Formatting doesn't affect the functionality of the code itself.

### Installation

```
pip install black
```

### Configure VS Code

1. Open Settings with `Ctrl+,` and click the Workspace tab.
2. Search `python.formatting.provider` and select `black` from the dropdown menu.
3. Then search `editor.formatOnSave` and enable by clicking the checkbox.

### Further Reading
1. [Consistent Python code with Black](https://www.mattlayman.com/blog/2018/python-code-black/)
2. [VS Code Setup Instructions](https://code.visualstudio.com/docs/python/editing#_formatting)


## Resources

* [Nine simple steps for better-looking python code](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)