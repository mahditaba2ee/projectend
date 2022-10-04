from itertools import product
from django.urls import reverse
from django.db import models
from Accounts.models import User
from django.utils.text import slugify

# Create your models here.


class CategoryModel(models.Model):
    name_category = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=200,unique=True)
    img = models.ImageField(upload_to='category/',null=True)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.name_category

        
    def get_absoulut_url(self):
        return reverse('category:searchcategory',args=(self.slug,))
        
    
class TypeProductModel(models.Model):
    category = models.ForeignKey(CategoryModel,models.CASCADE,related_name='type')
    name = models.CharField(max_length=50)

    slug = models.SlugField(max_length=100, unique=True, allow_unicode=True,blank=True, verbose_name='آدرس لینک',)

    def __str__(self) -> str:
        return f'{self.name}{self.category}'

    def save(self,*args,**kwargs):
        slug = self.category.slug+self.name
        self.slug =slug
        return super().save()
class BrandModel(models.Model):
    category = models.ForeignKey(CategoryModel,models.CASCADE,related_name='cbrand',null=True)
    name_brand = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200,unique=True,blank=True)
    def __str__(self):
        return self.name_brand
    def save(self,*args,**kwargs):
        
        self.slug = f'{self.category}-{self.name_brand}'
        return super().save()

    
class ProductModel(models.Model):
    user = models.ForeignKey(User,models.CASCADE,related_name='uproduct')
    category = models.ForeignKey(CategoryModel,models.CASCADE,related_name='cproduct')
    brand = models.ForeignKey(BrandModel,models.CASCADE,related_name='bproduct',null=True)
    type = models.ForeignKey(TypeProductModel,models.CASCADE,related_name='typeproduct',null=True,blank=True)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200,unique=True,null=True,blank=True)
    des = models.CharField(max_length=500)
    price = models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    like = models.ManyToManyField(User,blank=True)
    star = models.JSONField(default=dict,blank=True,null=True)
    special = models.BooleanField(default=False)
    like_count = models.IntegerField(default=0)

  
        
        



    
    def get_absoulut_url(self):
        return reverse('category:datails',args=(self.category.slug,self.brand.slug,self.slug))
        
    
    
    def save(self,*args,**kwargs):
        slug = str(self.id)
        self.slug=slugify(slug)
        super().save()
        

    def get_like_user(self):
        return self.like.count()
      
    class Meta:
        ordering =('-like_count',)
        

class ProductNotModels(models.Model):
    user = models.ForeignKey(User,models.CASCADE,related_name='upnot')
    product = models.ForeignKey(ProductModel,models.CASCADE,related_name='opnot',null=True)
    view = models.BooleanField(default=False)
    


class ImageProductModel(models.Model):
    product = models.ForeignKey(ProductModel,models.CASCADE,related_name='iproduct',null=True,blank=True)
    image = models.ImageField(upload_to='product/')
   

    def save(self,*args,**kwargs):
        self.image.name=f'{self.product.name}.png'

        return super().save()

class OrderModel(models.Model):
    usersender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='senderorder',null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='uorder')
    address = models.CharField(max_length=500,blank=True)
    phone = models.CharField(max_length=13,blank=True)
    name = models.CharField(max_length=50,blank=True)
    view = models.BooleanField(default=False)

    paid = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def total_price(self):
        return sum(item.get_cost() for item in self.oitems.all())
    class Meta:
        ordering =('view',)

class OrderItemsModel(models.Model):
    user_created = models.ForeignKey(User,models.CASCADE,related_name='ucreated',null=True)
    order = models.ForeignKey(OrderModel,models.CASCADE,related_name='oitems')
    product = models.ForeignKey(ProductModel,models.CASCADE,related_name='poitem')
    price = models.IntegerField()
    number = models.IntegerField(default=1)
    view = models.BooleanField(default=False)
    def get_cost(self):
        return int(self.number) * int(self.price)


class ImagdeSlidModel(models.Model):
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()

    def __str__(self):
        return str(self.id)
