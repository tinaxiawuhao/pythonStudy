from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hello world ! ")


def hello(request):
    context = {"name": "hello world"}
    return render(request, 'hello.html', context)


def runoob(request):
    views_name = "菜鸟教程"
    context = {"name": views_name}
    context['views_list']= ['菜鸟教程1', '菜鸟教程2', '菜鸟教程3']
    context['hello'] = 'Hello World Templates!'
    context['views_dict'] = {"name":"菜鸟教程2"}
    import datetime
    now = datetime.datetime.now()
    context['time'] = now
    views_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    context['views_str'] = views_str
    return render(request, 'runoob.html', context)
