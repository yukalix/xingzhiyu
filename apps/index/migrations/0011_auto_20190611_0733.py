# Generated by Django 2.1 on 2019-06-11 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_auto_20190611_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='url',
            field=models.CharField(default='', max_length=100, verbose_name='service链接'),
        ),
    ]
