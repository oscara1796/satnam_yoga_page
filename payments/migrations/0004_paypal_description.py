# Generated by Django 3.1.4 on 2021-02-14 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_paypal_sku'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypal',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
    ]
