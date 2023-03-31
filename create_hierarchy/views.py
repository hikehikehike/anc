import json
import random

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django_seed import Seed

from create_hierarchy.forms import EmployeeForm
from create_hierarchy.models import Employee

POSITION = [
    "god",
    "seo",
    "lead",
    "senior",
    "middle",
    "junior",
    "trainee",
]


def delete_db_and_create_god():
    Employee.objects.all().delete()
    god = Employee(name='GOD', position='god', hire_date='2022-01-01', email='johndoe@example.com')
    god.save()


def generate_json():
    got = Employee.objects.filter(manager=None).first()

    def create_json(employee):
        data = {
            "name": employee.name,
            "position": employee.position,
        }
        children = []
        for child in employee.children.all():
            children.append(create_json(child))
        if children:
            data["children"] = children
        return data

    tree_data = create_json(got)
    with open('static/treedata.json', 'w') as outfile:
        json.dump(tree_data, outfile)


def generate_db(request):
    delete_db_and_create_god()

    range_ = 50
    for ind, pos in enumerate(POSITION):
        if ind != 0:
            range_ *= 3
            emp = Employee.objects.filter(position=POSITION[ind - 1])

            seeder = Seed.seeder()
            seeder.add_entity(Employee, range_, {
                "name": lambda x: seeder.faker.first_name(),
                "position": pos,
                "manager": lambda x: random.choice(emp)
            })
            inserted_pks = seeder.execute()

    generate_json()

    return render(request, 'wait.html')


def index(request):
    return render(request, 'index.html')


class EmployeeListViews(generic.ListView):
    model = Employee
    fields = "__all__"
    paginate_by = 50
    ordering = ["id", "position", "name", "hire_date", "email", "manager"]


class EmployeeUpdateViews(generic.UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy("create_hierarchy:employee_list")
