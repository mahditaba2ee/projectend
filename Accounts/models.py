
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import MyUserManager


# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=200,unique=True)
    username = models.CharField(max_length=50,unique=True)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=500,blank=True)
    name =  models.CharField(max_length=50)
    family =  models.CharField(max_length=50)
    poster = models.ImageField(upload_to='poster/')
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =('username','phone')

    def __str__(self) -> str:
        return self.email
    
    def has_perm(self,perm,obj=None):
        return True
    
    def has_module_perms(self,app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin




class CompanyModel(models.Model):
    user = models.OneToOneField(User,models.CASCADE,related_name='cuser')
    name = models.CharField(max_length=20,null=True)
    national_card = models.ImageField()
    business_license = models.ImageField()
    verify = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} ------- is admin' 
        
    # def save(self,*args,**kwargs):
    #     self.verify =True
    #     return super().save(*args,**kwargs)
    #     with open(f'{self.user}/nationalcode',)
        

class OtpCodeModel(models.Model):
    phone = models.CharField(max_length=13)
    code = models.IntegerField(null=True)
    created = models.DateTimeField(auto_now_add=True)

from category.models import OrderModel

class NotifacationModel(models.Model):
    user = models.ForeignKey(User,models.CASCADE,related_name='usernoti')
    text = models.CharField(max_length=500,null=True)
    view = models.BooleanField(default=False)


    