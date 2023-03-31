# ANC

Django service for generating fake Hierarchy of Employee

Test user

Login: admin

Password: admin

## Installation

Python3 must be already installed

```shell
git clone https://github.com/hikehikehike/fake_csv
python3 -m venv venv
sourse venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Features

* Only authorized users can generating fake hierarchy, update and delete employee
* In "Hierarchy of Employee" user can see hierarchy
* In "List of Employee (detail)" user can sort or search
