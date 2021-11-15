# Quick start guide for Python projects

---

> :fire: First replace all NAME occurrences by final project name

## Start a new Python project
1. Install PyCharm :warning: via toolbox software
    - https://www.jetbrains.com/toolbox-app/
1. Install python 3
    - https://wiki.python.org/moin/BeginnersGuide/Download
1. Update pip
    - `curl https://bootstrap.pypa.io/get-pip.py | python3`
1. Install virtualenv
    - `pip3 install virtualenv`
1. Go to your dev folder and make a project folder in it
    - `mkdir my_awesome_project` -> go in it `cd my_awesome_project`
1. Start a new python env
    - `virtualenv -p python3 venv`
1. Active your environment
    - On UNIX: `source venv/bin/activate`
    - On Windows: `venv\Scripts\activate`
1. For deactivation
    - Simply type `deactivate`
1. Validate that you're running python 3+
    - `python --version`
1. Update pip with
    - `python -m pip install --upgrade pip`
1. For further installations you can simply run
    - `pip install pytest`
    - `pip install django`
    - and so on...
1. Then don't forget to put it in a requirements.txt for server installation
    - `pip freeze > requirements.txt`
