from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    text="Django Kurulumu: python -m pip install -e django <br> Proje Oluşturma: django-admin startproject mysite <br> App Ekleme: python manage.py startapp polls <br> Proje Yayına Alma: python manage.py runserver "
    #return HttpResponse("Deneme Test Sayfası : %s." % text) # Yazı yazdı sadece
    context = {'text': text}
    return render(request, 'index.html', context)