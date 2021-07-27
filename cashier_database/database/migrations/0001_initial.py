# Generated by Django 3.2.5 on 2021-07-22 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("public_id", models.CharField(max_length=225, unique=True)),
                ("country", models.CharField(max_length=225, null=True)),
                ("state", models.CharField(max_length=225, null=True)),
                ("city", models.CharField(max_length=225, null=True)),
                ("address", models.CharField(max_length=225, null=True)),
                ("postal_code", models.CharField(max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Phone",
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
                ("public_id", models.CharField(max_length=225, unique=True)),
                (
                    "phone_numbers",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None, unique=True
                    ),
                ),
                (
                    "phone_fax",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, region=None
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Type",
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
                ("public_id", models.CharField(max_length=225, unique=True)),
                (
                    "type",
                    models.IntegerField(
                        choices=[(0, "Member"), (1, "Staff"), (2, "Owner")], default=0
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Accounts",
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
                ("is_deleted", models.BooleanField(default=False)),
                ("create_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField()),
                ("public_id", models.CharField(max_length=225, unique=True)),
                ("avatar", models.ImageField(null=True, upload_to="accounts/")),
                (
                    "gender",
                    models.IntegerField(
                        choices=[(0, "Male"), (1, "Female")], default=0
                    ),
                ),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="database.address",
                    ),
                ),
                (
                    "phone",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="database.phone"
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="database.type"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
