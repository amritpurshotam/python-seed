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

#### Sorting Imports on Save

1. Add the following lines to the `.vscode/settings.json` file
    ```
    "editor.codeActionsOnSave": {
        "source.organizeImports": true
    }
    ```
2. Since `black` and `isort` have different formatting rules which will [conflict](https://github.com/microsoft/vscode-python/issues/6933) with each other, add the following lines to the `.vscode/settings.json` file as well
    ```
    "python.sortImports.args": [
        "--multi-line=3",
        "--trailing-comma",
        "--force-grid-wrap=0",
        "--use-parentheses",
        "--line-width=88",
    ]
    ```

### Further Reading
1. [Consistent Python code with Black](https://www.mattlayman.com/blog/2018/python-code-black/)
2. [VS Code Setup Instructions](https://code.visualstudio.com/docs/python/editing#_formatting)

## Linting
Linting highlights syntactical and stylistic problems in your Python source code, which oftentimes helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors.

### Installation

```
pip install flake8
```

### Configure VS Code

1. Open Setting with `Ctrl+,` and click the Workspace tab.
2. Search `python.linting.flake8Enabled` and enable by clicking the checkbox.
3. The next two settings are defaults but to ensure the project uses it regardless of a users settings, add the following lines in the `.vscode/settings.json` file.
    ```
    "python.linting.enabled": true,
    "python.linting.lintOnSave": true
    ```

### Further Reading

1. [Flake8 Extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)
2. [Linting Python in VS Code](https://code.visualstudio.com/docs/python/linting)

## Static Type Checking

### Installation
```
pip install mypy
```

### Configure VS Code

1. Open Setting with `Ctrl+,` and click the Workspace tab.
2. Search `python.linting.mypyEnabled` and enable by clicking the checkbox

## Resources

* [Nine simple steps for better-looking python code](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)