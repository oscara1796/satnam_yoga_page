# Generated by Django 3.1.4 on 2021-02-14 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypal',
            name='image',
            field=models.ImageField(null=True, upload_to='plans', verbose_name='Imagen'),
        ),
    ]
