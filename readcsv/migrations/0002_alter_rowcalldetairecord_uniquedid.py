# Generated by Django 5.0.1 on 2024-01-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("readcsv", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rowcalldetairecord",
            name="uniquedid",
            field=models.CharField(
                max_length=30, unique=True, verbose_name="идентификатор вызова"
            ),
        ),
    ]
