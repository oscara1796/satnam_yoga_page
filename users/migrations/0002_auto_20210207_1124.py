# Generated by Django 3.1.4 on 2021-02-07 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='paypalSubscriptionId',
            field=models.CharField(blank=True, max_length=255, verbose_name='Paypal Subscirpción id'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='stripeCustomerId',
            field=models.CharField(blank=True, max_length=255, verbose_name='Stripe Cliente id'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='stripeSubscriptionId',
            field=models.CharField(blank=True, max_length=255, verbose_name='Stripe Subscirpción id'),
        ),
    ]
