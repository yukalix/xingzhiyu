# Generated by Django 2.1 on 2019-06-11 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0012_auto_20190611_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(max_length=200, upload_to='team/%Y')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('introduce', models.TextField(max_length=160, verbose_name='介绍')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('is_delete', models.BooleanField(default=True, verbose_name='是否在职')),
            ],
            options={
                'verbose_name': '我们的团队',
                'verbose_name_plural': '我们的团队',
            },
        ),
        migrations.AlterField(
            model_name='information',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='是否使用'),
        ),
        migrations.AlterField(
            model_name='service',
            name='is_delete',
            field=models.BooleanField(default=True, verbose_name='是否使用'),
        ),
    ]
