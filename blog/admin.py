from django.contrib import admin

from blog.models import Royxat,Yangiliklar,Bizhaqimizda_rasm,\
    SONGI_YILLARDA_BAJARILGAN_ISHLAR_XAJMI,FuterManzil


# Register your models here.
@admin.register(Royxat)
class RoyxatAdmin(admin.ModelAdmin):
    list_display = ['ism']
@admin.register(FuterManzil)
class ManzilAdmin(admin.ModelAdmin):
    list_display = ['email']
@admin.register(Yangiliklar)
class YangilikAdmin(admin.ModelAdmin):
    list_display = ['nom']
@admin.register(Bizhaqimizda_rasm)
class Bizhaqimizda_rasmAdmin(admin.ModelAdmin):
    list_display = ['nom']
@admin.register(SONGI_YILLARDA_BAJARILGAN_ISHLAR_XAJMI)
class SONGI_YILLARDA_BAJARILGAN_ISHLAR_XAJMIAdmin(admin.ModelAdmin):
    list_display = ['nom']
