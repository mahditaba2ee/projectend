
from dataclasses import field, fields
from pyexpat import model
from django import forms
from .models import CompanyModel, OtpCodeModel, User
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UsercreateForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email','phone','username')
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 !=password2:
            raise forms.ValidationError('password not math')
        if len(password2) < 7:
            raise forms.ValidationError('password not 8 ')

        return password1
    


    def save(self, commit= False):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    



class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = []


class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = CompanyModel
        fields = ('national_card','business_license')
        

