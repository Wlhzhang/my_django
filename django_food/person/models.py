from django.db import models

# Create your models here.
from dinner.models import DinnerInfo
from polls.models import MyUser


class SingDinner(models.Model):
    sing_user = models.ForeignKey(MyUser,on_delete=models.PROTECT)
    dinner = models.ForeignKey(DinnerInfo,on_delete=models.PROTECT)
    apply_reason = models.CharField('申请理由',max_length=100)
    remark = models.CharField('备注',max_length=100)
    class Meta:
        db_table = 'sing_table'
        # 修改后台页面上的名称
        verbose_name = '饭局报名表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.apply_reason


class City(models.Model):
    name = models.CharField('名称', max_length=50)
    parent_id = models.IntegerField('父类id')
    area_sort = models.IntegerField('排序')
    city_type = models.IntegerField('类型')