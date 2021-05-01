from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from contents.models import Content
from home.models import Setting, ContactFormu, ContactFormMessage, SliderPhoto
from django.contrib import messages

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = SliderPhoto.objects.all()[:3]
    context = {'setting': setting,
               'page':'home',
               'sliderdata':sliderdata}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslarimiz.html', context)



def iletisim(request):

    if request.method == 'POST': # form post edildiyse
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage() # model ile bağlantı kur
            data.name = form.cleaned_data['name'] #formdan bilgiti al
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save() #veritabanına kaydet
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz")
            return HttpResponseRedirect('/iletisim')

    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting,'form':form}
    return render(request, 'iletisim.html', context)