from django.urls import path

from . import views

urlpatterns = [
    path("erse/",views.home_screen_view, name="home"),
    path("news/",views.news, name="news"),
    path("ev/",views.ev, name="ev"),
]
