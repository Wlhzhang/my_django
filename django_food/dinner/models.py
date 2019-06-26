from django.db import models

# Create your models here.
from polls.models import MyUser


class DinnerInfo(models.Model):
    dinner_title = models.CharField('饭局标题',max_length=20)
    price = models.DecimalField('饭局价格',max_digits=8,decimal_places=2)
    number = models.IntegerField('人数')
    dinner_date = models.DateField('活动时间')
    deadline = models.DateField('截止时间')
    activities_play = models.CharField('活动玩法',max_length=30)
    activities_photo = models.ImageField('活动照片')
    intro = models.CharField('简介',max_length=200)
    user_id = models.ForeignKey(MyUser,on_delete=models.PROTECT)
    class Meta:
        db_table = 'dinner_info'
