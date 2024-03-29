# Generated by Django 2.2 on 2019-06-26 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DinnerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dinner_title', models.CharField(max_length=20, verbose_name='饭局标题')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='饭局价格')),
                ('number', models.IntegerField(verbose_name='人数')),
                ('dinner_date', models.DateField(verbose_name='活动时间')),
                ('deadline', models.DateField(verbose_name='截止时间')),
                ('activities_play', models.CharField(max_length=30, verbose_name='活动玩法')),
                ('activities_photo', models.ImageField(upload_to='', verbose_name='活动照片')),
                ('intro', models.CharField(max_length=200, verbose_name='简介')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'dinner_info',
            },
        ),
    ]
