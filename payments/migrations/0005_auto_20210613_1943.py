# Generated by Django 3.1.4 on 2021-06-14 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0004_paypal_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paypal',
            name='paypalPlanId',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Paypal plan id'),
        ),
    ]
