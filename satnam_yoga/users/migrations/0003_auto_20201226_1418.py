# Generated by Django 3.1.4 on 2020-12-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stripeCustomerId',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='stripeSubscriptionId',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
