[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![build](https://github.com/amritpurshotam/python-seed/workflows/build/badge.svg)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

# python-seed

Seed project implementing Python best practices with setup instructions. This is mainly for VS Code users.

## Virtual Environment

### Installation of Python

Install `pyenv-win` by following instructions [here](https://github.com/pyenv-win/pyenv-win) or `pyenv` on Mac with `brew install pyenv`.

To install and activate your desired version of python, run the following in the project workspace (here we use 3.11.9)

```
pyenv install 3.11.9
pyenv local 3.11.9
pyenv exec python -m venv .venv

.\.venv\Scripts\activate.ps1 # Windows
source ./.venv/bin/activate # Mac
```

To find the exact version use the following example (for e.g. we're looking for the latest version of python 3.11).

```
pyenv install -l | select-string 3.11 # Windows
pyenv install -l | grep 3.11 # Mac
```

In case the version you're looking for is missing make sure to run

```
pyenv update # Windows
brew upgrade pyenv # Mac
```

### Installation of project

Make sure you're using python 3.11.9 in your virtual environment and it's activated.

```cmd
python -m pip install --upgrade pip setuptools wheel
pip install -e .[dev,test]
```

After the first command VS Code should ask if you want to activate that environment which you should accept.
The following lines make sure you've activated your environment in your powershell command line as well where
you then install the project.

## Formatting and Linting

Formatting makes code easier to read by human beings by applying specific rules and conventions for line spacing, indents, spacing around operators, and so on. Formatting doesn't affect the functionality of the code itself.

Linting highlights syntactical and stylistic problems in your Python source code, which oftentimes helps you identify and correct subtle programming errors or unconventional coding practices that can lead to errors.

### Installation

```cmd
pip install ruff
```

### Configure VS Code

Make sure to install the ruff extension then set the following in the `.vscode/settings.json`

```json
{
  "[python]": {
    "editor.formatOnSave": true, // format code on save
    "editor.codeActionsOnSave": {
      "source.fixAll": "explicit", // will automatically fix errors if it can
      "source.organizeImports": "explicit" // sort imports on save
    },
    "editor.defaultFormatter": "charliermarsh.ruff" // format with ruff
  },
  "ruff.importStrategy": "fromEnvironment", // use the version of ruff in the venv
  "ruff.organizeImports": true
}
```

## Static Type Checking

### Installation

```
pip install mypy
```

### Configure VS Code

Install the `mypy` vs code extension then set the following

```json
{
  "mypy-type-checker.importStrategy": "fromEnvironment"
}
```

## Continuous Integration with Github Actions

### Further Reading

1. [Using Python with GitHub Actions](https://help.github.com/en/actions/language-and-framework-guides/using-python-with-github-actions)

## Resources

- [Nine simple steps for better-looking python code](https://towardsdatascience.com/nine-simple-steps-for-better-looking-python-code-87e5d9d3b1cf)
- [Python Best Practices](https://sourcery.ai/blog/python-best-practices/)
- [Collection of git hooks by Mpho Mphego](https://blog.mphomphego.co.za/blog/2019/10/03/Why-you-need-to-stop-using-Git-Hooks.html)
