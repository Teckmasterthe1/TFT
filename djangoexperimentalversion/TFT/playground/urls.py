from django.urls import path
from . import views

#URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('main/', views.say_main),
    path('main/calculator/', views.say_calculator),
    path('main/calculator/basicmath/', views.say_basicmath)
]