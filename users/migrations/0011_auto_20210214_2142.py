# Generated by Django 3.1.4 on 2021-02-15 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20210214_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='active',
            field=models.CharField(choices=[('A', 'Activo'), ('T', 'temporal'), ('C', 'Cancell')], default='C', max_length=2, verbose_name='Status'),
        ),
    ]
