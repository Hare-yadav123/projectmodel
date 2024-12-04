# Generated by Django 5.0.2 on 2024-03-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeModel",
            fields=[
                ("Emp_id", models.AutoField(primary_key=True, serialize=False)),
                ("Name", models.CharField(max_length=100)),
                ("Email", models.CharField(max_length=100)),
                ("Phone", models.BigIntegerField()),
                ("Address", models.CharField(max_length=100)),
                ("DOB", models.CharField(max_length=100)),
                ("Joine_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]