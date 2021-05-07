from django.http import HttpResponse
from django.shortcuts import render

from contents.models import Menu
from home.models import Setting, UserProfile


# Create your views here.


def index(request):
    setting = Setting.objects.get(pk=1)
    current_user = request.user  # Acces user session
    profile = UserProfile.objects.get(user_id=current_user.id)
    menu = Menu.objects.all()
    context = {'menu': menu,
               'setting': setting,
               'profile': profile,
               }
    return render(request, 'user_profile.html', context)