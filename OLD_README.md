# cake-shop-py-api
Cake Shop API Services in Python Flask

# Install Python 3

# Instal PIP3
pip / pip3 is a de facto standard package-management system used to install and manage software packages written in Python. 

# Instal pipx
pipx is a tool to help you install and run end-user applications written in Python.  

```
brew install pipx
```

# Install virtualenv
virtualenv is a CLI tool that needs a Python interpreter to run. If you already have a Python 3.5+ interpreter the best is to use pipx to install virtualenv into an isolated environment. 

```
pipx install virtualenv
```

### Notification  
Note: '/Users/<userName>/.local/bin' is not on your PATH environment variable. These apps will not be globally accessible until your PATH is updated. Run `pipx ensurepath` to automatically add it, or manually modify your PATH in your shell's config file (i.e. ~/.bashrc).  

```
pipx ensurepath
```

### Verify  
```
virtualenv --help
```

## Setup Virtual Environment

```
virtualenv env
source env/bin/activate
```

## Install Flask Base Project

```
pip3 install flask flask-sqlalchemy
```

--------

```
pip3 install pipenv
```

```
pipenv shell
```

```
python3 app.py
```

pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy


Lang Error

```
Warning: the environment variable LANG is not set!
We recommend setting this in ~/.profile (or equivalent) for proper expected behavior.
Warning: Python 3.9 was not found on your system…
Neither 'pyenv' nor 'asdf' could be found to install Python.
You can specify specific versions of Python with:
$ pipenv --python path/to/python
```


```
vi ~/.zshrc
```

```
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
```

```
pipenv --python 3.8.2
```