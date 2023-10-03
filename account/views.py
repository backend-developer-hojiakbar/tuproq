from django.contrib.auth.forms import UserCreationForm
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from account.forms import UserEditForm, ProfileEditForm, UserRegisterationForm
from .models import Profile

# Create your views here.
def profileedit(request):
    return render(request, "tuproq/profile_edit.html", context={})
def deshboard_view(request):
    user = request.user
    context ={
        "user": user
    }
    return render(request,"registration/user_profile.html",context)

def edit_user(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user,data=request.POST)
        profile_form =ProfileEditForm(instance=request.user.profile,
                                      data = request.POST,
                                      files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form =ProfileEditForm(instance=request.user.profile)
    return render(request, "tuproq/profile_edit.html", {"user_form": user_form, "profile_form": profile_form})

def deshboard_view(request):
    users = request.user
    profiles = Profile.objects.all()
    print(users)
    profile_info = Profile.objects.get(user=users)
    context={
        "user":users,
        "profile_info": profile_info
    }
    return render(request,"registration/user_profile.html",context)

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = "tuproq/register.html"

def user_register(request):
    if request.method == "POST":
        user_form = UserRegisterationForm(request.POST)
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data["password"])
        new_user.save()
        context = {
            "new_user" : new_user
        }
        return render(request,"tuproq/register_done.html",context=context)
    else:
        user_form = UserRegisterationForm()
        context = {
            "user_form": user_form
        }
        return render(request, "tuproq/register.html", context=context)
