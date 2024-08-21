# Generated by Django 4.2.2 on 2024-08-20 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_payments"),
    ]

    operations = [
        migrations.AddField(
            model_name="payments",
            name="link",
            field=models.URLField(
                blank=True, max_length=400, null=True, verbose_name="Ссылка на оплату"
            ),
        ),
        migrations.AddField(
            model_name="payments",
            name="session_id",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="ID сессии"
            ),
        ),
    ]
