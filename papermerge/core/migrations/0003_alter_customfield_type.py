# Generated by Django 4.2.13 on 2024-10-15 13:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_customfield_documenttype_documenttypecustomfield_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customfield",
            name="type",
            field=models.CharField(max_length=50),
        ),
    ]