# Generated by Django 4.1 on 2022-08-22 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gi_association_application_status",
            options={"verbose_name_plural": "GI_Association_application_status"},
        ),
        migrations.AlterModelOptions(
            name="gi_user_application_status",
            options={"verbose_name_plural": "User Application Status"},
        ),
        migrations.AlterModelOptions(
            name="gi_user_reges", options={"verbose_name_plural": "User Registration"},
        ),
    ]