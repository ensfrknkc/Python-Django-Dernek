from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from contents.models import Content, Menu,Images

from home.models import Setting, ContactFormu, ContactFormMessage, SliderPhoto
from django.contrib import messages

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Content.objects.all()[:3]
    menu = Menu.objects.all()
    latestnews= Content.objects.all().order_by('menu_id','update_at')[:3]

    context = {'setting': setting,
               'menu': menu,
               'page':'home',
               'sliderdata':sliderdata,
               'latestnews':latestnews}
    return render(request, 'index.html', context)

def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    context = {'setting': setting,'menu': menu,}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    context = {'setting': setting,'menu': menu,}
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
    menu = Menu.objects.all()
    context = {'setting': setting,'form':form,'menu': menu,}
    return render(request, 'iletisim.html', context)

def menu_contents(request,id,slug):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    menudata = Menu.objects.get(pk = id)
    contents = Content.objects.filter(menu_id=id)
    context = {'contents': contents,'setting': setting,'menu': menu,'menudata':menudata}
    return render(request, 'contents.html', context)

def content_detail(request,id,slug):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    content = Content.objects.get(pk=id)
    images = Images.objects.filter(content_id=id)
    context = {'content':content,
               'setting': setting,
               'menu': menu,
               'images': images, }
    return render(request, 'content_detail.html', context)