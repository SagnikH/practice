from django.urls import path

from . import views

urlpatterns = [
    path('add', views.res, name='result'),
    path('', views.calcu, name='home'),
    path('foot/', views.test, name='test'),

]