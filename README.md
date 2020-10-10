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


