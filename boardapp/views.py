from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.shortcuts import render, redirect, get_object_or_404
from .models import BoardModel
# Create your views here.

def signupfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    try:
      # createが実行された時点で既にユーザーは作成保存される(saveメソッドは必ずしも必要ない)
      user = User.objects.create_user(username, '', password)
      return render(request, 'signup.html', {'some':500})
    except IntegrityError:
      return render(request,'signup.html', {'error': 'このユーザーは既に登録されています'})

  return render(request, 'signup.html', {'some':500})

def loginfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('list')
    else:
      return render(request, 'login.html', {})
  return render(request, 'login.html', {})      

@login_required
def listfunc(request):
  object_list = BoardModel.objects.all()
  return render(request, 'list.html',{'object_list' :object_list})
  
def logoutfunc(request):
  logout(request)
  return redirect('login')

@login_required
def detailfunc(request, pk):
  object = get_object_or_404(BoardModel, pk=pk)
  return render(request, 'detail.html', {'object':object})

def goodfunc(request, pk):
  object = BoardModel.objects.get(pk=pk)
  object.good += 1
  object.save()
  return redirect('list')

def readfunc(request, pk):
  object = BoardModel.objects.get(pk=pk)
  username = request.user.get_username()
  if username in object.readtext:
    return redirect('list')
  else:
    object.read = object.read + 1
    object.readtext = object.readtext + ' ' + username
    object.save()
    return redirect('list')