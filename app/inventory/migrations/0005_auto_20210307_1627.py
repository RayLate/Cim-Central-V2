# Generated by Django 3.1.7 on 2021-03-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("inventory", "0004_auto_20210307_1606")]

    operations = [
        migrations.AlterField(
            model_name="device",
            name="remarks",
            field=models.TextField(blank=True, max_length=200),
        )
    ]
