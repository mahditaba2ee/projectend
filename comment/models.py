from django.db import models
from Accounts.models import User
from category.models import ProductModel
# Create your models here.

class CommentModel(models.Model):
    user = models.ForeignKey(User,models.CASCADE,related_name='ucomment')
    product = models.ForeignKey(ProductModel,models.CASCADE,related_name='pcomment')
    to_user =   models.CharField(max_length=50,null=True)

    body = models.CharField(max_length=500)
    is_replay = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True)

class ReplayCommentModel(models.Model):
    comment = models.ForeignKey(CommentModel,models.CASCADE,related_name='rcomment')
    user = models.ForeignKey(User,models.CASCADE,null=True)
    to_user =   models.CharField(max_length=50,null=True)
    body = models.CharField(max_length=500)
    is_replay = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True,null=True)
    view = models.BooleanField(default=False)

    def __str__(self):
        return self.body