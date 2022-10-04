
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User,OtpCodeModel,NotifacationModel,CompanyModel
from .forms import *
from django.contrib.auth.models import Group 
# Register your models here.



class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UsercreateForm

    list_display = ('email','username','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None,{'fields':('email','username','phone','password')}),
        ('personal info',{'fields':('name','family','address','poster')}),

        ('permissions',{'fields':('is_admin','is_active','is_superuser')}),
    
    )
    add_fieldsets = (
        (None,{'classes':('wide',),
        'fields':('email','username','phone','password1','password2')}),

        )
    
    search_fields = ('email',)
    ordering = ('last_login',)
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User,UserAdmin)
admin.site.register(OtpCodeModel)
admin.site.register(NotifacationModel)
admin.site.register(CompanyModel)