# Generated by Django 5.1.2 on 2024-10-29 12:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("foodcartapp", "0049_order_comments"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="comments",
            field=models.TextField(
                blank=True, default="", null=True, verbose_name="Комментарии"
            ),
        ),
    ]
