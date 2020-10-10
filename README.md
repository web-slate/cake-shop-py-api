# cake-shop-py-api
Cake Shop API Services in Python Flask

# Install Python 3

# Instal PIP3
pip / pip3 is a de facto standard package-management system used to install and manage software packages written in Python. 

## Install PIP Env

```
pip3 install pipenv
```

# Create Project Config File. 

```
pipenv shell
```

# Install Flash Project.
```
pipenv install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
pipenv install requests --upgrade
```

## Error: Lang Error

```
Warning: the environment variable LANG is not set!
We recommend setting this in ~/.profile (or equivalent) for proper expected behavior.
```

### Edit RC File and Update Language
```
vi ~/.zshrc
or
vi ~/.bashrc
```

### Error: 
```
export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
```

## Error: Python Error

```
Warning: Python 3.9 was not found on your system…
Neither 'pyenv' nor 'asdf' could be found to install Python.
You can specify specific versions of Python with:
$ pipenv --python path/to/python
```

```
pipenv --python 3.8.2
```

## Run Application

```
python3 app.py
```

## Create DB

```
(cake-shop-py-api) ➜  cake-shop-py-api git:(main) ✗ python3
Python 3.8.2 (default, Aug 25 2020, 09:23:57)
[Clang 12.0.0 (clang-1200.0.32.2)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import db
>>> db.create_all()
```

Error:
```
TypeError: __init__() got an unexpected keyword argument 'strict'
```

Reference: https://www.youtube.com/watch?v=PTZiDnuC86g