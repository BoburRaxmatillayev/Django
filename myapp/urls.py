from django.urls import path
from .views import home_page, about_page, service_page, contact_page

urlpatterns = [
    path('uy/',home_page, name='uy'),
    path('biz haqimizda/', about_page ,name='biz haqimizda'),
    path('servisexizmati/', service_page ,name='servisexizmati'),
    path('kontaktlar/', contact_page ,name='kontaktlar'),
]