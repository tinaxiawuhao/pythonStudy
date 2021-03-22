# 认证模块
from django.contrib import auth
# 对应数据库
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def createUser(request):
    User.objects.create(username='runboo', password='123')
    User.objects.create_user(username='runbooo', password='123')
    User.objects.create_superuser(username='runboooo', password='123', email='runboo@163.com')
    return HttpResponse("ok")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    user_obj = auth.authenticate(username=username, password=password)
    print(user_obj.username)
    if not user_obj:
        return redirect("/testModel/login/")
    else:
        auth.login(request, user_obj)
        path = request.GET.get("next") or "/testModel/index/"
        print(path)
        return redirect(path)


def logout(request):
    ppp = auth.logout(request)
    print(ppp)  # None
    return redirect("/testModel/login/")


@login_required
def index(request):
    return HttpResponse("index页面。。。")
