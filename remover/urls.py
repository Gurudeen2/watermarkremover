from django.urls import path
from . import views 

urlpatterns =[
    path("", views.home, name="home"),
    path("removebgimg/", views.remove_img_background, name="removebgimg"),
    path("addwatermark/", views.addwatermark, name="addwatermark"),
]