
from cProfile import label
from django import forms
from .models import ProductModel,CategoryModel
from django.forms import Textarea,TextInput
class AddProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields = ('name','des','price')


class AddCtegoryForm(forms.ModelForm):
    class Meta:
        model=CategoryModel
        fields=('name_category','slug','img')
        # widgets={
        #     'name_category':TextInput(attrs={'class':'text-input','placeholder':'نام کالا'}),
        #     'slug':TextInput(attrs={'class':'text-input','placeholder':'لینک'}),
        #     'img':TextInput(attrs={'class':'text-input','placeholder':'نام کالا'})

        # }
        # labels={
        #     'name_category':('نام '),
        #     'slug':('آدرس '),
        #     'img':('عکس ها ')

        # }