from django.contrib.auth.models import User
# from django.forms import forms
from django import forms

from account.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
class UserRegisterationForm(forms.ModelForm):
    password = forms.CharField(label="Parol",
                               widget=forms.PasswordInput)
    password_2 = forms.CharField(label="Parolni takrorlang",
                               widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username","first_name","email"]
    def clean_password2(self):
        data = self.cleaned_data
        if data["password"] != data["password2"]:
            raise forms.ValidationError("ikkala parolingiz bir biriga teng bo'lishi kerak")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth","photo"]


