# Generated by Django 2.2 on 2019-07-01 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': '用户信息表', 'verbose_name_plural': '用户信息表'},
        ),
    ]
