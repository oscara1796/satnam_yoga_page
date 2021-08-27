# Generated by Django 3.2.5 on 2021-08-27 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210827_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yogaclass',
            name='hour',
        ),
        migrations.AddField(
            model_name='yogaclass',
            name='hour_to_end',
            field=models.TimeField(null=True, verbose_name='Termina'),
        ),
        migrations.AddField(
            model_name='yogaclass',
            name='hour_to_start',
            field=models.TimeField(null=True, verbose_name='Comienza'),
        ),
    ]
