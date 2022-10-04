
from functools import cache
from itertools import count
import json
from multiprocessing.pool import AsyncResult
from nis import cat
from operator import length_hint
from os import lstat
import re
import string
from typing import List
from unicodedata import category

from django import views
import django
from django.http import HttpRequest, HttpResponse, JsonResponse, QueryDict
from django.shortcuts import redirect, render
from django.urls import reverse_lazy ,reverse
from django.views import View
from .models import *
from .forms import AddProductForm,AddCtegoryForm
from django.core.files.base import ContentFile
from django.utils.text import slugify
from .cart import Cart
from Accounts.views import UserProfileView
from django.contrib import messages
from comment.models import CommentModel,ReplayCommentModel
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .send_email import send_email
from .utils import shopping_cart


# Create your views here.

class CategoryView(View):
    def get(self,request):
        buys = []
        imageslide = ImagdeSlidModel.objects.get(id=1)

        if request.session.get('cart') is not None:
            buys = shopping_cart(request)
        most_like_product = ProductModel.objects.all()[:6]
        # products = []
        
        # x=0
        # for product in most_like_product:
        #     if (int(product.star)) >= 4:
        #         products.append(product)
        #         x +=1
        #         if x == 7:
        #             return
        

        # most_like_product = products
        home=True
        categories = CategoryModel.objects.all()
        return render(request,'category/home.html',{'home':home,'most_like_product':most_like_product,'categories':categories,'buys':buys,'imageslide':imageslide})

# class SearchView2(View):
#     def get(self,request,strproduct):
#         type = TypeProductModel.objects.get(slug=strproduct)
#         product = ProductModel.objects.filter(type=type).values()

#         product = list(product)
#         return JsonResponse(product,safe=False)
class AddProductView(LoginRequiredMixin,View):
    def get(self,request):
        category = CategoryModel.objects.filter(available=True)
        brands = BrandModel.objects.all()
        type = TypeProductModel.objects.all()
        return render(request,'category/add_product.html',{'category':category,'brands':brands,'type':type})
    
    def post(self,request):
        form =AddProductForm(request.POST)
        category = CategoryModel.objects.get(name_category=request.POST['category'])
        brand = BrandModel.objects.get(category=category,name_brand = request.POST['brand'])
        
        try:
            if form.is_valid():
                cd = form.cleaned_data
                product = ProductModel.objects.create(user =request.user,name=cd['name'], category=category,brand=brand,des=cd['des'],price=cd['price'])
                product.slug=slugify(f'{product.id}-{product.name}')
                
                product.save()
                
            file = request.FILES.getlist("images[]")
            
            for img in file:
                ImageProductModel.objects.create(product=product,image=img)
                
            messages.success(request,'محصول اضافه شد','success')
        except:
            messages.info(request,'محصول اضافه نشد','info')

        return redirect('category:addproduct')
       

class ProductDetailsView(View):
    def get(self,request,product_slug,*args,**kwargs):
        print(product_slug)
        product = ProductModel.objects.get(slug=product_slug)
        buys = []
        
        if request.session.get('cart') is not None:
            buys = shopping_cart(request)
        products = ProductModel.objects.filter(category=product.category)
        comment = CommentModel.objects.filter(product = product,is_replay=False)
        images = ImageProductModel.objects.filter(product=product)
        print(comment)
        # comment_replay = ReplayCommentModel.objects.filter(comment = comment)
        
        return render(request,'category/details_product.html',{'product':product,'comment':comment,'images':images,'products':products,'buys':buys})



class CartView(View):
    def get(self,request):
        cart = Cart(request)
        return render(request,'category/cart2.html',{'cart':cart})
       
class CartAddView(View):
    def post(self,request):
        cart = Cart(request)
        
        product = ProductModel.objects.get(slug=request.POST.get('slug'))
        number = request.POST['number']
        cart = Cart(request)
       

        try:
            if number !="":
                number = int(number)
            else:
                number = 1
            cart.Add(product,number)

            return JsonResponse({'status':'ok','cart_value':request.session['cart']})

        except:
            return JsonResponse({'status':'err'})
        
class CartRemoveView(View):
    def post(self,request):
        product = ProductModel.objects.get(id=request.POST['id'])
        cart = Cart(request)
        cart.Remove(product)
        return JsonResponse({'status':'ok'})


class OrderView(LoginRequiredMixin,View):
    def get(self,request):
        a=OrderModel.objects.filter(user = request.user)
        if request.user.address =='':
            messages.info(request,'برای ثبت سفارش لطفا اطلاعات خود را وارد نمایید','info')
            return redirect('/accounts/profie?next=orderview')
        
        order_create = OrderModel.objects.create(user = request.user,address = request.user.address,phone=request.user.phone,name=f'{request.user.name}{request.user.family}')
        cart = Cart(request)
        
        global  OrderItems
        my_lst=[]
        for order in cart:
            pruduct = ProductModel.objects.get(id=order['product'].id)
            
            my_lst.append(order['product'].user.id)
            OrderItems =  OrderItemsModel.objects.create(order = order_create,user_created =  order['product'].user ,product=pruduct,price=int(order['product'].price),number=int(order['number']))
        #در اینجا باید کاربر به صفحه پرداخت هدایت شود
        del request.session['cart']
        request.session.modified = True
        my_set = set(my_lst)
        for id in my_set:
           
            user = User.objects.get(id=id)
            for order in cart:
                if order['product'].user.id == user.id:
                    ProductNotModels.objects.create(user = user,product=order['product'])
        return HttpResponse(my_lst)


        
    
    
        
class SendOrderView(View):
    def get(self,request):
        if request.user.is_superuser:
            users = User.objects.filter(is_admin=True)
            orders = OrderModel.objects.filter(usersender=None,view=False)
            return render(request,'category/send_order.html',{'orders':orders,'users':users})

        if request.user.is_admin:
            user = User.objects.get(id = request.user.id)
            notification =  OrderItemsModel.objects.filter(user_created = user)       
            noti_view = notification.filter(view=True).order_by('order')
            noti_not_view = notification.filter(view=False)
             
            print(noti_not_view.exists())
        
            my_lst=[]
            for n in notification:
                my_lst.append(n.order.id)
                
            my_set=set(my_lst)
            
            return render(request,'category/not_product.html',{'noti_view':noti_view,'noti_not_view':noti_not_view,'order_id':my_set})

    def post(self,request):
        id = request.POST['id']
        
        notification =  OrderItemsModel.objects.get(id= id)     
        notification.view=True
        notification.save()
        order = OrderModel.objects.get(id = notification.order.id)
        items = OrderItemsModel.objects.filter(order= order)
        my_lst=[]
        all_from_user=1
        for o in items:
            my_lst.append(o.product.name)
            if o.user_created != request.user:
                all_from_user=0
            if o.view == False:
                return
        try:
            send_email(my_lst,order.id,order.user.email,order.address,order.user.name,order.user.family)
            if all_from_user == 1:
                order.usersender=request.user

        except:
            notification.view=False
            notification.save()
            return JsonResponse({'status':'not_net'})
        
        
        order.view = True
        order.save()
            
        
        
        send_email(my_lst,order.id,order.user.email,order.address,order.user.name,order.user.family)
        return JsonResponse({'status':'ok','all':all_from_user})
      


class OldOrderView(View):
    def get(self,request):
        if request.user.is_superuser:
            orders = OrderModel.objects.filter(view=True)
            return render(request,'category/old_orders.html',{'orders':orders})
        else:
            orders = OrderModel.objects.filter(usersender=request.user)
            return render(request,'category/old_orders.html',{'orders':orders})


class SubmitOrderView(View):
    def post(self,request):
        orderid = request.POST.get('id')
        order = OrderModel.objects.get(id = orderid)
        order.view=True
        order.save()
        messages.success(request,'سبد خرید تایید شد','success')
        return JsonResponse({'status':'ok'})
        


class BackOrderView(View):
    def post(self,request):
        orderid = request.POST.get('id')
        order = OrderModel.objects.get(id = orderid)
        order.usersender=None
        order.save()
        messages.success(request,'سبد خرید برگشت داده شد','success')
        return JsonResponse({'status':'ok'})



class SendOrderUserView(View):
    def post(self,request):
        iduser = request.POST.get('iduser')
        idorder = request.POST.get('idorder')
        user = User.objects.get(id = iduser)
        order = OrderModel.objects.get(id = idorder )
        order.usersender = user
        order.save()
        messages.success(request,'سبد خرید تایید شد','success')
        return JsonResponse({'status':'ok'})


class CommentAddView(View):
    def post(self,request):
        id = request.POST.get('id')
        commentbody = request.POST.get('comment')
        productid = request.POST.get('productid')
        product = ProductModel.objects.get(id=productid)
        
        if id == '':
            comment = CommentModel.objects.create(user=request.user,product = product,body=commentbody)
            if commentbody[0] == '@':
                user = commentbody.split(' ',1)[0][1::]
                if User.objects.filter(username= user).exists():
                    comment.to_user = user
                    comment.save()
                    return JsonResponse({'status':'comment'})
                


        if id !='':
            c=CommentModel.objects.get(id=id)
            user = commentbody.split(' ',1)[0][1::]
            
            ReplayCommentModel.objects.create(user = request.user ,to_user=user, comment=c,body=commentbody)
            
            
        
        messages.success(request,'نظر شما ثبت شد','success')

        return JsonResponse({'status':'comment'})
from django.db.models import Q
class SearchView(View):
    def get(self,request,strproduct):

        buys =[]
        if request.session.get('cart') is not None:
            buys = shopping_cart(request)
        categories = CategoryModel.objects.all()

        try:
            try:
                type = TypeProductModel.objects.get(slug = strproduct)
                products = ProductModel.objects.filter(Q(type=type))

            except:
                products = ProductModel.objects.filter(Q(name__contains=strproduct)|Q(des__contains=strproduct))
            return render(request,'category/search.html',{"products":products,'categories':categories,'buys':buys})
        except:
            return render(request,'category/search.html',{'categories':categories,'buys':buys})

        



        category = CategoryModel.objects.get(name_category=slug)
        if brand_slug is not None:
            brand = BrandModel.objects.get(slug=brand_slug)
            products = ProductModel.objects.filter(brand=brand)

        else:
            products = ProductModel.objects.filter(category=category)

        
        lenorders=0
        if request.user.is_authenticated:
            lenorders = len(OrderModel.objects.filter(usersender=request.user,view=False))
        images=[]
        for p in products:
            images.append(ImageProductModel.objects.filter(product=p).first()) 
        
        category = CategoryModel.objects.all()
        return render(request,'category/list_category.html',{"products":products,'images':images,'lenorders':lenorders,'category':category})

class SearchCategoryView(View):
    def get(self,request,category_slug):
        category = CategoryModel.objects.get(slug=category_slug)
        buys = []
        if request.session.get('cart') is not None:
            buys = shopping_cart(request)
        products = ProductModel.objects.filter(category = category)
        return render(request,'category/category_search.html',{"products":products,'buys':buys})

        
class ChoiseView(View,LoginRequiredMixin):
    
    def post(self,request):
        category = CategoryModel.objects.get(name_category=request.POST['value'])
        type = TypeProductModel.objects.filter(category=category)
        brand = BrandModel.objects.filter(category=category)
        mylst=[]
        mylst2=[]
        for b in brand:
            mylst.append(b.name_brand)
        for t in type:
            mylst2.append(t.name)
        return JsonResponse({'status':mylst,'mylst2':mylst2})

from .tasks import remove_like

class LikeView(View):
    def post(self,request):
        

        id_product = request.POST['id']
        is_like = request.POST['is_like']
        product = ProductModel.objects.get(id = id_product )

        if (is_like == 'dislike'):
            # try:
            #     remove_like.delay(id_product,request.user.id)
            # except:
            #     print()
            
                
            # return JsonResponse({'status':'dislike','like_number':product.like.count()})

            if request.user in product.like.all():
                product.like.remove(request.user)
                product.like_count -=1
                product.save()
                return JsonResponse({'status':'dislike','like_number':product.like.count()})

            else:
                return JsonResponse({'status':'like_before','like_number':product.like.count()})
        if (is_like =='like'):
            
            if request.user not in product.like.all():
                product.like.add(request.user)
                product.like_count +=1
                product.save()

                return JsonResponse({'status':'like','like_number':product.like.count()})
            else:
                return JsonResponse({'status':'like_before','like_number':product.like.count()})

class StarAddView(View):
    
    

    def post(self,request):

        product_id = request.POST['id']
        product = ProductModel.objects.get(id = product_id)
        username = request.user.username
        star_count = request.POST['count']
        

        if not request.user.is_authenticated: 
            if star_count =='start':
                return JsonResponse({'star':product.star})
 
            return JsonResponse({'status':'notauth'})
        if star_count !='start':
            product.star[str(username)] =str( star_count)
            product.save()
        return JsonResponse({'star':product.star,'username':username})
        

class SharePostView(View):
    def post(self,request):
        users = User.objects.all()
        return render(request,'category/share.html',{'users':users})


class AddBrandView(View):
    def post(self,request):
        cd = request.POST
        try:
            category = CategoryModel.objects.get(name_category=cd['category'])
            BrandModel.objects.create(category=category,name_brand=cd['name_brand'])
            return JsonResponse({'status':'ok'})
        except:
            return JsonResponse({'status':'err'})



class AddCategoryView(View):
    def get(self,request):
        form = AddCtegoryForm
        return render(request,'category/add_category.html',{"form":form})
    def post(self,request):
        cd = request.POST
        media = request.FILES
        try:
            category = CategoryModel.objects.create(name_category=cd['name'],slug=cd['slug'],img=media['img'])
            if (request.POST.get('avalable',False)=='on'):
                category.available=True
                category.save()
            messages.success(request,'کالا افزوده شد','success')
            return redirect('category:addproduct') 

        except:
            
            messages.info(request,'کالا افزوده نشد','info')
            return redirect('category:addcategory') 


class AddTypeView(View):
    def post(self,request):
        cd = request.POST
        try:
            category = CategoryModel.objects.get(name_category=cd['category'])
            TypeProductModel.objects.create(category=category,name=cd['name_type'])
            return JsonResponse({'status':'ok'})
        except:
            return JsonResponse({'status':'err'})

