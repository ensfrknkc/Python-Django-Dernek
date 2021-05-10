from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import json
# Create your views here.
from contents.models import Content, Menu,Images,Comment

from home.models import Setting, ContactFormu, ContactFormMessage, UserProfile, FAQ
from home.forms import SearchForm, SignUpForm
from django.contrib import messages

def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Content.objects.all()[:3]
    news = Content.objects.filter(type='News', status='True').order_by('-id')[:5]
    notice = Content.objects.filter(type='Notice', status='True').order_by('-id')[:5]
    comments = Comment.objects.filter(status='True').order_by('update_at')[:3]
    menu = Menu.objects.all()
    latestnews= Content.objects.all().filter(type='News', status='True').order_by('update_at')[:3]

    context = {'setting': setting,
               'menu': menu,
               'sliderdata': sliderdata,
               'latestnews': latestnews,
               'news': news,
               'notice': notice,
               'comments': comments,
              }
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
    content = Content.objects.get(menu_id=id)
    context = {'content': content,'setting': setting,'menu': menu,'menudata':menudata}
    return render(request, 'contents.html', context)

def content_detail(request,id,slug):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    content = Content.objects.get(pk=id)
    images = Images.objects.filter(content_id=id)
    comments = Comment.objects.filter(content_id=id, status='True')
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

def content_search_auto(request):
  if request.is_ajax():
    q = request.GET.get('term', '')
    content = Content.objects.filter(title__icontains=q)
    results = []
    for rs in content:
      content_json = {}
      content_json = rs.title
      results.append(content_json)
    data = json.dumps(results)
  else:
    data = 'fail'
  mimetype = 'application/json'
  return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Login Hatası ! Kullanıcı adı yada Şifre hatalı.")
            return HttpResponseRedirect('/login')

    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    context = { 'menu': menu,
                'setting': setting,
                }
    return render(request, 'login.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            #Create data in profile table for user
            current_user = request.user
            data = UserProfile()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            messages.success(request, "Hoşgeldiniz... Sitemize başarılı bir şekilde üye oldunuz.")
            return HttpResponseRedirect('/')


    form = SignUpForm()
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    context = {'menu': menu,
                'setting': setting,
               'form': form,
                }
    return render(request, 'signup.html', context)


def faq(request):
    setting = Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    faq = FAQ.objects.all().order_by('ordernumber')
    context = {'menu': menu,
               'setting': setting,
               'faq': faq,
               }
    return render(request, 'faq.html', context)