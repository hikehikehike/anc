# Generated by Django 4.1.7 on 2023-03-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("create_hierarchy", "0005_alter_employee_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="position",
            field=models.CharField(
                choices=[
                    ("god", "God"),
                    ("seo", "Seo"),
                    ("lead", "Lead"),
                    ("senior", "Senior"),
                    ("middle", "Middle"),
                    ("junior", "Junior"),
                    ("trainee", "Trainee"),
                ],
                max_length=255,
            ),
        ),
    ]