# Generated by Django 4.0.2 on 2022-02-24 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_payment_delete_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='User_id',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
