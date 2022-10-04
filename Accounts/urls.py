from django.urls import path
from .views import *
from .checkinregister import *

app_name='accounts'

urlpatterns=[

    path('register',UserRegisteView.as_view(),name='register'),
    path('check/email/',check.as_view(),name='emailexist'),
    path('check/phone/',CheckPhone.as_view(),name='checkphone'),
    path('check/username/',CheckUsername.as_view(),name='checkusername'),
    path('verifycode',OtpCodeView.as_view(),name='verifycode'),
    path('login',LoginView.as_view(),name='login'),
    path('logout',LogoutView.as_view(),name='logout'),
    path('profie',UserProfileView.as_view(),name='profile'),
    path('notification',NotifacationView.as_view(),name='notification'),
    path('company/sumbit/',CompanyView.as_view(),name='company'),
    path('company/verify/',CopmanyVerifyView.as_view(),name='company_verify'),
    path('notifications/',NotificationsView.as_view(),name='notifications'),
    path('usernames',UsernameView.as_view(),name='usernames'),


  


    #resetpassword
    path('password/reset/',PasswordResetView.as_view(),name='passwordreset'),
    path('password/reset/done',PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/',PasswordResetConfirm.as_view(),name='password_reset_confirm'),
    path('password/reset/complate',PasswordResetComplateView.as_view(),name='password_reset_complate'),
    

   

    


]