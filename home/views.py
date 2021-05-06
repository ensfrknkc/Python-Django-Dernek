from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from contents.models import Content, Menu,Images,Comment

from home.models import Setting, ContactFormu, ContactFormMessage
from home.forms import SearchForm
from django.contrib import messages

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Content.objects.all()[:3]
    menu = Menu.objects.all()
    latestnews= Content.objects.all().order_by('update_at')[:3]

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
    comments = Comment.objects.filter(content_id=id,status='True')
    context = {'content': content,
               'setting': setting,
               'menu': menu,
               'images': images,
               'comments': comments}
    return render(request, 'content_detail.html', context)


def content_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            setting = Setting.objects.get(pk=1)
            menu = Menu.objects.all()
            query = form.cleaned_data['query'] #formdaki bilgiyi al
            contents = Content.objects.filter(title__icontains=query) #select * from content where title like %query%
            #return HttpResponse(contents)
            context = {'contents': contents,
                       'menu': menu,
                       'setting': setting,
                       }
            return render(request, 'content_search.html',context)

    return HttpResponseRedirect('/')