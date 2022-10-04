

import pickle
from email.mime import base
from time import sleep
from celery import Celery,Task
from celery import shared_task




from .models import *
from django.http import HttpRequest, HttpResponse, JsonResponse, QueryDict
from .forms import *
from .cart import Cart
from django.utils.decorators import method_decorator
from HasanAbad.celery_conf import celery_app as c
import json
from Accounts.models import User


@shared_task
def remove_like(id_product,id_user):
    product = ProductModel.objects.get(id = id_product)
    user = User.objects.get(id = id_user)
    if user in product.like.all():
        product.like.remove(user)
        product.like_count +=1
        product.save()
        return None
    return False

     

        
        
  