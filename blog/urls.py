from django.urls import path
from .views import *
urlpatterns = [
    path('', AsosiyPage, name="asosiy"),
path('biz_haqimizda/', Biz_haqimizda, name="biz_haqimizda"),
path('rahbariyat/', Biz_haqimizda_rahbariyat, name="rahbariyat"),
path('hamkor/', hamkor, name="hamkor"),
path('Foter/', Foter, name="Foter"),
path('ishla/', ishla, name="ishla"),
path('Hujjatlar/', Hujjatlar, name="Hujjatlar"),
path('labaratoriya/', Labaratoriya, name="labaratoriya"),
path('yangiliklar/', yangiliklar, name="yangiliklar"),
path('news_detel/<int:id>',news_detel, name="news_detel"),


]