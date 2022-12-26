from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def signupfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    # createが実行された時点で既にユーザーは作成保存される(saveメソッドは必ずしも必要ない)
    user = User.objects.create_user(username, '', password)
  return render(request, 'signup.html', {'some':100})