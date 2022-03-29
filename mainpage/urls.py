from django.urls import path

from . import views

app_name = 'mainpage'
urlpatterns = [
    path('', views.index, name='index'),
    path('u/<str:short_url>', views.goto, name='goto'),
    path('create', views.create, name='create')
]