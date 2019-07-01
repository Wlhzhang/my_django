# Generated by Django 2.2 on 2019-07-01 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20, unique=True, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='用户邮箱')),
                ('head_image', models.FileField(null=True, upload_to='tmp/', verbose_name='用户头像')),
                ('sex', models.CharField(max_length=10, null=True, verbose_name='性别')),
                ('career', models.CharField(max_length=50, null=True, verbose_name='职业')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='地址')),
                ('intro', models.CharField(max_length=200, null=True, verbose_name='简介')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
