# Generated by Django 5.0 on 2023-12-14 19:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receipts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipt",
            name="total",
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]