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
2. Since `black` and `isort` have different formatting rules which will [conflict](https://sourcery.ai/blog/python-best-practices/) with each other, add the following lines to the `setup.cfg` file
    ```
    [isort]
    multi_line_output=3
    include_trailing_comma=True
    force_grid_wrap=0
    use_parentheses=True
    line_length=88
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
4. Standardise settings between `black` and `flake8` add the following to a `setup.cfg` file in the root of the project
    ```
    [flake8]
    max-line-length = 88
    max-complexity = 18
    select = B,C,E,F,W,T4,B9
    ignore = E266, E501, W503
    ```

### Further Reading

1. [Flake8 Extensions](https://github.com/DmytroLitvinov/awesome-flake8-extensions)
2. [Linting Python in VS Code](https://code.visualstudio.com/docs/python/linting)
3. [Standardisation of Black and Flake8](https://medium.com/staqu-dev-logs/keeping-python-code-clean-with-pre-commit-hooks-black-flake8-and-isort-cac8b01e0ea1)

## Static Type Checking

### Installation
```
pip install mypy
```

### Configure VS Code

1. Open Setting with `Ctrl+,` and click the Workspace tab.
2. Search `python.linting.mypyEnabled` and enable by clicking the checkbox

## Areas to Improve

1. Need to find a way to manage dev and prod dependencies i.e. the linting, formatting, type checking, etc tools are not needed to actually run the code in a production environment. Pipenv seems to solve this but need to investigate further

## Continuous Integration with Github Actions

### Further Reading

1. [Using Python with GitHub Actions](https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions)

## Resources

* [Nine simple steps for better-looking python code](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)
* [Python Best Practices](https://sourcery.ai/blog/python-best-practices/)
