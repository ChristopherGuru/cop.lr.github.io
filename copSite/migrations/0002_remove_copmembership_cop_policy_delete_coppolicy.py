# Generated by Django 4.1.2 on 2023-02-16 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("copSite", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="copmembership", name="cop_policy",),
        migrations.DeleteModel(name="CopPolicy",),
    ]