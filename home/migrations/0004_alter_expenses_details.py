# Generated by Django 4.2.4 on 2023-08-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_alter_expenses_amount_alter_orders_amount_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expenses", name="details", field=models.TextField(),
        ),
    ]
