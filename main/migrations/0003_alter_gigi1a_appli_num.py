# Generated by Django 4.1 on 2022-08-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_gigi1a"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gigi1a",
            name="Appli_num",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
