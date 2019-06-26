from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self,username,password):
        # 验证用户名是否为空
        if not username:
            raise ValueError('用户名不能为空')

        user = self.model(
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,username,password):
        # 创建超级用户
        user = self.create_user(
            username,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    username = models.CharField('用户名',max_length=20,unique=True)
    email = models.EmailField('用户邮箱')
    head_image = models.FileField('用户头像',null=True,upload_to='tmp/')
    sex = models.CharField('性别',null=True,max_length=10)
    career = models.CharField('职业',null=True,max_length=50)
    address = models.CharField('地址',null=True,max_length=50)
    intro = models.CharField('简介',null=True,max_length=200)
    is_admin = models.BooleanField

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []  # 创建超级用户时使用

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        db_table = 'user'
