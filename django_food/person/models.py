from django.db import models

# Create your models here.
from dinner.models import DinnerInfo
from polls.models import MyUser


class SingDinner(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.PROTECT)
    dinner = models.ForeignKey(DinnerInfo,on_delete=models.PROTECT)
    apply_reason = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    class Meta:
        db_table = 'sing_table'