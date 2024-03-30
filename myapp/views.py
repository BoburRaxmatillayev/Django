from django.shortcuts import render
from django.http import HttpResponse 


def home_page(request):
    return HttpResponse("Salom Dunyo !")

def about_page(request):
    return HttpResponse("Bu yerda biz haqimizda bilib olishingiz mumkin !")

def service_page(request):
    return HttpResponse("Bu yerda biz mijozlarga xizmat ko'rsatamiz !")

def contact_page(request):
    return HttpResponse("Bu yerda biz bilan bog'lanishingiz mumkin!")

