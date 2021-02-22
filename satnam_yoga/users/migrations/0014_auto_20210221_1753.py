# Generated by Django 3.1.4 on 2021-02-21 23:53

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210221_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='active',
            field=models.CharField(choices=[(users.models.statusChoices['ACTIVE'], 'ACTIVO'), (users.models.statusChoices['TRIAL'], 'TEMPORAL'), (users.models.statusChoices['CANCELLED'], 'CANCELADO')], default=users.models.statusChoices['CANCELLED'], max_length=1, verbose_name='Status'),
        ),
    ]
