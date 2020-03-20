from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import BoardModel

class BoardCreate(CreateView):
     template_name = 'create.html'
     model = BoardModel
     fields = ('title', 'content', 'author', 'images')
     success_url = reverse_lazy('list')


def signupfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, 'signup.html', {'error': 'このユーザーは登録されています'})
        except:
            user = User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some': 100})
    return render(request, 'signup.html', {'some': 100})

def loginfunc(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a login success page.
            return redirect('list')
        else:
            # Return an 'invalid login' error message.
            return redirect('login')
    return render(request, 'login.html')

@login_required    
def listfunc(request):
    object_list = BoardModel.objects.all() 
    return render(request, 'list.html', {'object_list': object_list})

def detailfunc(request, pk):
    object = BoardModel.objects.get(pk=pk)
    return render(request, 'detail.html', {'object': object})

def goodfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post.good += 1
    post.save()
    return redirect('list')

def readfunc(request, pk):
    post = BoardModel.objects.get(pk=pk)
    post2 = request.user.get_username()
    if post2 in post.readtext:
        return redirect('list')
    else:
        post.read += 1
        post.readtext += ' ' + post2
        post.save()
        return redirect('list')

def logoutfunc(request):
    logout(request)
    return redirect('login')
