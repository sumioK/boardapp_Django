from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.db import IntegrityError
from django.shortcuts import render, redirect
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
      return render(request, 'login.html', {'context':'logged in'})      
    else:
      return render(request, 'login.html', {'context':'not logged in'})
  return render(request, 'login.html', {'context':'get method'})      

def listfunc(request):
  return render(request, 'list.html',{})