from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView,\
    PasswordResetView,PasswordChangeView,PasswordChangeDoneView,\
    PasswordResetConfirmView,PasswordResetCompleteView,\
    PasswordResetDoneView,PasswordResetForm,PasswordChangeForm

from .views import deshboard_view, SignUpView, edit_user, user_register

urlpatterns = [
    path("login/",LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("user/",deshboard_view,name="profile"),
    path("password-change/",PasswordChangeView.as_view(),name="password_change"),
    path("password-change-done/", PasswordChangeDoneView.as_view(), name="password_change_done"),
    path("password-reset/", PasswordResetView.as_view(), name="password_reset"),
    path("password-reset/done/", PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("password-reset/complete/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    path("sing-up/",user_register,name="sign_up"),
    path("user-edit/",edit_user, name="user_edit")

]