# Generated by Django 2.1 on 2019-06-11 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_auto_20190611_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='address',
            field=models.CharField(default='', max_length=72, null=True, verbose_name='企业地址'),
        ),
        migrations.AlterField(
            model_name='information',
            name='email',
            field=models.EmailField(default='admin@admin.admin', max_length=254, null=True, verbose_name='企业邮箱'),
        ),
        migrations.AlterField(
            model_name='information',
            name='icp',
            field=models.CharField(default='', max_length=100, null=True, verbose_name='企业备案号'),
        ),
        migrations.AlterField(
            model_name='information',
            name='introduce',
            field=models.CharField(default='', max_length=360, null=True, verbose_name='企业描述'),
        ),
        migrations.AlterField(
            model_name='information',
            name='mobile',
            field=models.CharField(default='', max_length=12, null=True, verbose_name='企业电话'),
        ),
        migrations.AlterField(
            model_name='information',
            name='name',
            field=models.CharField(default='星之羽网络科技有限公司', max_length=36, null=True, verbose_name='企业名称'),
        ),
        migrations.AlterField(
            model_name='information',
            name='qq',
            field=models.CharField(default='', max_length=12, null=True, verbose_name='企业QQ'),
        ),
    ]