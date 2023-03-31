# ANC

Django service for generating fake Hierarchy of Employee

## Installation

Python3 must be already installed

```shell
git clone https://github.com/hikehikehike/anc/tree/main
python3 -m venv venv
sourse venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### How to use

1. Press login
2. Generate fake Employees
3. Now you can see hierarchy and list of employee

### Features

* Only authorized users can generating fake hierarchy, update and delete employee
* In "Hierarchy of Employee" user can see hierarchy
* In "List of Employee (detail)" user can sort or search
