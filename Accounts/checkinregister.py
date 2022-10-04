from .models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
import re

# def check(email):
#     user = User.objects.filter(email=email).exists()
#     if user == 0:
#         return JsonResponse({'emailexist':'0'})
        
#     else:
#         return JsonResponse({'emailexist':'1'})

class check(View):
    
    def post(self,request):
        
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        email = request.POST['email']
        if re.fullmatch(regex, email):
            user = User.objects.filter(email=email).exists()
            if user == 0:
                return JsonResponse({'emailexist':'0'})
            else:
                return JsonResponse({'emailexist':'2'})
        else:
            return JsonResponse({'emailexist':'1'})
            
    
class CheckPhone(View):
    def post(self,request):
        phone = request.POST['phone']
        mobile_regex = "^09(1[0-9]|3[1-9])-?[0-9]{3}-?[0-9]{4}$"
        if(re.search(mobile_regex, phone)):
            user = User.objects.filter(phone=phone).exists()
            if user==0:
                return JsonResponse({'phoneexist':'0'})
            else:
                return JsonResponse({'phoneexist':'2'})

        else:
            return JsonResponse({'phoneexist':'1'})


class CheckUsername(View):
    def post(self,request):
        usernamefilter="=)(*&^%$#@!~/-+|:?><"
        username = request.POST['username']
        if username[0]=='_' or username[0] in usernamefilter:
                return JsonResponse({'usernameexist':'1'})
        for ch in username:
            if ch in usernamefilter:
                return JsonResponse({'usernameexist':'1'})

        user = User.objects.filter(username=username).exists()
        if user==0:
            return JsonResponse({'usernameexist':'0'})
        else:
            return JsonResponse({'usernameexist':'2'})



# def check_username(username):
#         usernamefilter="=)(*&^%$#@!~/-+|:?><"
#         username = username
#         if username[0]=='_' or username[0] in usernamefilter:
#                 return False
#         for ch in username:
#             if ch in usernamefilter:
#                 return False

#         user = User.objects.filter(username=username).exists()
#         if user==0:
#             return True
#         else:
#             return False




    


        