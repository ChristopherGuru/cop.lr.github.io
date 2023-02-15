# Generated by Django 4.1.6 on 2023-02-15 11:24

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CopPolicy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "i_accept",
                    models.BooleanField(
                        default=True,
                        verbose_name="I ACCEPT the Terms and Condition of the Church of Pentecos",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CopMembership",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "suffix",
                    models.CharField(
                        choices=[
                            ("MR", "Mr"),
                            ("MRS", "Mrs"),
                            ("SIS", "Sis"),
                            ("BRO", "Bro"),
                            ("DEC", "Dec"),
                            ("DNS", "Dns"),
                            ("ELD", "Eld"),
                        ],
                        max_length=4,
                        null=True,
                    ),
                ),
                ("f_name", models.CharField(max_length=65)),
                ("m_name", models.CharField(max_length=65)),
                ("l_name", models.CharField(max_length=65)),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("city_of_birth", models.CharField(max_length=100)),
                ("district_of_birth", models.IntegerField()),
                ("county_of_orgin", models.CharField(max_length=65)),
                ("nationality", models.CharField(max_length=65)),
                ("current_address", models.CharField(max_length=65)),
                (
                    "phone_num",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("occupation", models.CharField(max_length=65)),
                ("history_of_salvation", models.CharField(max_length=150)),
                ("if_yes", models.CharField(max_length=150)),
                ("church", models.CharField(max_length=65)),
                ("location", models.CharField(max_length=65)),
                ("who_conducted_the_baptism", models.CharField(max_length=65)),
                ("type_of_baptism", models.CharField(max_length=65)),
                ("date_of_baptism", models.DateField(blank=True, null=True)),
                ("father_name", models.CharField(max_length=65)),
                ("f_occupation", models.CharField(max_length=65)),
                ("f_religious_affiliation", models.CharField(max_length=65)),
                ("mother_name", models.CharField(max_length=65)),
                ("m_occupation", models.CharField(max_length=65)),
                ("m_religious_affiliation", models.CharField(max_length=65)),
                ("employment_type", models.CharField(max_length=65)),
                ("institution", models.CharField(max_length=100)),
                ("s_location", models.CharField(max_length=65)),
                ("graduation_year", models.DateField(blank=True, null=True)),
                ("achivement", models.CharField(max_length=65)),
                ("signed", models.CharField(max_length=56)),
                ("this_certifies_that", models.CharField(max_length=65)),
                ("offical_signed", models.CharField(max_length=65)),
                ("date", models.DateTimeField(auto_now_add=True)),
                ("approved", models.CharField(max_length=65)),
                ("date_approved", models.DateTimeField(auto_now_add=True)),
                (
                    "cop_policy",
                    models.ManyToManyField(blank=True, to="copSite.coppolicy"),
                ),
            ],
        ),
    ]
