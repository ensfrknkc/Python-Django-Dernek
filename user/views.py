from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
from contents.models import Menu, ContentForm
from home.models import Setting, UserProfile


# Create your views here.
from user.forms import UserUpdateForm, ProfileUpdateForm
from contents.models import Comment, Content


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


def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) #request.user is user data
        #"instance=request.user.userprofile" comes from "userprofile" model -> OneToOneField relation
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Your account has been updated!")
            return redirect('/user')
    else:
        menu = Menu.objects.all()
        setting = Setting.objects.get(pk=1)
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile) #"userprofile" model->OneToOneField relation with user
        context = {
            'menu' : menu,
            'user_form' : user_form,
            'profile_form' : profile_form,
            'setting' : setting,
        }
        return render(request, 'user_update.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) #important
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.warning(request, 'Please correct the error below.'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        menu = Menu.objects.all()
        setting = Setting.objects.get(pk=1)
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form, 'menu': menu, 'setting': setting
        })


@login_required(login_url='/login') #check login
def comments(request):
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {
        'menu' : menu,
        'setting' : setting,
        'comments' : comments,
    }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login') #check login
def deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted...')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login') #check login
def contents(request):
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    current_user = request.user
    contents = Content.objects.filter(user_id=current_user.id)
    context = {
        'menu' : menu,
        'setting' : setting,
        'contents' : contents,
    }
    return render(request, 'user_contents.html', context)


@login_required(login_url='/login') #check login
def addcontent(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Content() # model ile bağlantı kur
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.type = form.cleaned_data['type']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save() #veritabanına kaydet
            messages.success(request, 'Your Content Insterted Successfuly')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.warning(request, 'Your ContentForm Error :' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        menu = Menu.objects.all()
        setting = Setting.objects.get(pk=1)
        form = ContentForm()
        context = {
            'menu': menu,
            'setting': setting,
            'form': form,
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login') #check login
def contentedit(request,id):
    content = Content.objects.get(id=id)
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Content Updated Successfuly')
            return HttpResponseRedirect('/user/contents')
        else:
            messages.warning(request, 'Content Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/addcontent')
    else:
        menu = Menu.objects.all()
        setting = Setting.objects.get(pk=1)
        form = ContentForm(instance=content)
        context = {
            'menu': menu,
            'setting': setting,
            'form': form,
        }
        return render(request, 'user_addcontent.html', context)


@login_required(login_url='/login') #check login
def contentdelete(request,id):
    current_user = request.user
    Content.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Content deleted...')
    return HttpResponseRedirect('/user/contents')