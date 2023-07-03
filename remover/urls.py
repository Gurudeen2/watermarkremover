from django.urls import path
from .views import removewatermark

urlpatterns =[
    path("", removewatermark, name="home"),
]