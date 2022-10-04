


import json
import re
from secrets import choice
from unicodedata import name
from django.contrib import messages
from django.conf import settings
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render ,redirect
from django.views import View
from category.models import OrderModel
from .forms import UsercreateForm,UserLoginForm,CompanyForm
from django.contrib.auth import views as auth_view
from .models import CompanyModel, User , OtpCodeModel,NotifacationModel
from random import randint
from django.core.mail import send_mail
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse_lazy
import string
from comment.models import CommentModel, ReplayCommentModel



# Create your views here.


class UserRegisteView(View):
    def get(Self,request):
        return render(request,'accounts/user_register2.html')
    
    def post(self,request):

        form = UsercreateForm(request.POST)

        if form.is_valid():

            
            cd = form.cleaned_data
            email = cd['email']
            phone = cd['phone']
            password = cd['password1']
            username = cd['username']
            
            code = randint(10000,99999)
            otp_exist=OtpCodeModel.objects.filter(phone=phone)
            if otp_exist is not None:
                otp_exist.delete()
            OtpCodeModel.objects.create(phone=phone,code=code)
            send_mail('verify code',str(code),settings.EMAIL_HOST_USER,(email,))
            messages.success(request,'ایمیل حاوی کد تایید برای شما ارسال شد','success')
            
            request.session['userinfo'] = {
                'email':email,
                'phone':phone,
                'password':password,
                'username':username,
            }
                      
            return redirect('accounts:verifycode')
       

        messages.success(request,'لطفا مقادیر را بررسی کنید','info')
         
        return render(request,'accounts/user_register2.html',{'form':form})

class OtpCodeView(View):
    def get(self,request):
        phone , email=  request.session['userinfo']['phone'],request.session['userinfo']['email']
        return render(request,'accounts/user_verfy.html',{'phone':phone,'email':email})
    
    def post(self,request):
        info = request.session['userinfo']
        code = request.POST['code']
        otp = OtpCodeModel.objects.get(phone = info['phone'])
      
        if (str(otp.code) == str(code)):
            User.objects.create_user(username = info['username'] , email = info['email'],phone = info['phone'],password = info['password'])
            otp.delete()
            return JsonResponse({'code':'valid'})
        
        else:
            return JsonResponse({'code':'invalid'})


class LoginView(View):
    def get(self,request):
        
        return render(request,'accounts/login.html')
    
    def post(self,request):
        
        form =UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            username = cd['username'].lower()
            password = cd['password']
            user = authenticate(request,email=username , password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'شما با موفقیت وارد شدید','success')
                return redirect('category:category')
            else:
                messages.info(request,'رمز عبور یا نام کاربری اشتباه است','info')
                return redirect('accounts:login')
        else:
            messages.info(request,'عملیات با خطا مواجه شد','info')
            return redirect('accounts:login')
        

class LogoutView(View):
    def get(self ,request):
        logout(request)
        messages.success(request,'شما با موفقیت خارج شدید','success')
        return redirect('accounts:login')





class PasswordResetView(auth_view.PasswordResetView):
    template_name = 'accounts/reset/password_reset.html'
    email_template_name = 'accounts/reset/email.html'
    success_url=reverse_lazy('accounts:password_reset_done')

class PasswordResetDoneView(auth_view.PasswordResetDoneView):
    template_name = 'accounts/reset/password_reset_done.html'


class PasswordResetConfirm(auth_view.PasswordResetConfirmView):
    template_name='accounts/reset/password_reset_confirm.html'
    success_url=reverse_lazy('accounts:password_reset_complate')
    
    

class PasswordResetComplateView(auth_view.PasswordResetCompleteView):
    template_name = 'accounts/reset/password_reset_complate.html'


class UserProfileView(View):
    def get(self,request):
        
        return render(request,'accounts/profile.html')
    
    def post(self,request):
        
        info = request.POST
        user = User.objects.get(id = request.user.id)
        user.email = request.user.email
        user.phone = request.user.phone
        user.name = info['name']
        user.family = info['family']
        user.address = info['address']
        user.save()
        if request.GET.get('next') =='orderview':
            return redirect('category:order')
        return redirect('category:category')
class NotifacationView(View):
    def get(self,request):
        myorders = OrderModel.objects.filter(usersender=request.user,view=False)
        # for order in myorders:
        #     order.view = True
        #     order.save
        return render(request,'accounts/noti.html',{'myorders':myorders})
    def post(self,request):
        idorder = request.POST.get('idorder')
        iduser = request.POST.get('iduser')



from django.core.files.storage import FileSystemStorage
def password():
    char = string.ascii_letters + string.punctuation + string.digits
    passcode = ''.join(choice(char) for x in range(randint(8,16)))
    return passcode


class CompanyView(View):
   

    def get(self,request):
        return render(request,'accounts/company.html')

    def post(self,request):
        user = request.user
        national_card = request.FILES.get('national_card')
        national_card_fss = FileSystemStorage()
        national_card_file = national_card_fss.save(f'company/{request.user.username}/national_card{password()}.jpg',national_card)
        national_card_url = national_card_fss.url(national_card_file)
       
        business_license = request.FILES.get('business_license')
        business_license_fss = FileSystemStorage()
        business_license_file = business_license_fss.save(f'company/{request.user.username}/business_license{password()}.jpg',business_license)
        business_license_url = business_license_fss.url(business_license_file)
        namecompany = request.POST.get('namecompany')
       
        try:
            CompanyModel.objects.create(user = user,national_card=national_card_url,business_license=business_license_url,name = namecompany)
            messages.success(request,'درخواست شما ثبت شد و بس از تایید شما قادر به افزودن کالا در سایت می باشید')
            return redirect('accounts:company')
        except:
            messages.success(request,'مشکلی به وجود امده است یا شما قبلا در سایت ثبت نام کرده اید ')
            return redirect('accounts:company')


class CopmanyVerifyView(View):
    email_text = 'شرکت شما در سایت ثبت شده است و شما قادر میباشید تا آگهی ثبت و سفارشات را دریافت نمایید'
    def get(self,request):
        companies = CompanyModel.objects.filter(verify = False)
        return render(request,'accounts/company_verify.html',{'companies':companies})

    def post(self,request):
        id = request.POST['id']
        company = CompanyModel.objects.get(id = id)
        company.verify = True
        company.save()
        user = User.objects.get(id = company.user.id)
        user.is_admin= True
        
        user.save()
        send_mail('تاییذیه شرکت شما ',self.email_text,settings.EMAIL_HOST_USER,(company.user.email,))
        messages.success(request,'شرکت ثبت شد','success')
        return JsonResponse({'status':'ok'})


class NotificationsView(View):
    def get(self,request):
        comments = ReplayCommentModel.objects.filter(to_user = request.user.username,view=False)
        comments_tag = CommentModel.objects.filter(to_user = request.user.username)
        
        comments_view = ReplayCommentModel.objects.filter(to_user = request.user.username,view=True)
        return render(request,'accounts/notifications.html',{'comments':comments,'comments_view':comments_view,'comments_tag':comments_tag})
    
    def post(self,request):
        comments = ReplayCommentModel.objects.filter(to_user = request.user.username)
        for c in comments:
            c.view =True
            c.save()
        return JsonResponse({'status':'ok'})


class UsernameView(View):
    def post(self,request):
        cd =request.POST['value'][1::]
        
        users = User.objects.filter(username__contains=cd)
        lst_user=[]
        for user in users:
            lst_user.append(user.username)
        print('9'*99)
        print(lst_user)
        return JsonResponse({'users':lst_user})