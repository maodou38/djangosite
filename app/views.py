from django.http import HttpResponse
from app.forms import MomentForm
from django.http import HttpResponseRedirect
from django.urls import reverse # django2.0 把原来的 django.core.urlresolvers 包 更改为了 django.urls包，所以我们需要把导入的包都修改一下就可以了。
from django.shortcuts import render

import os


# 定义处理函数
def welcome(request):
    return HttpResponse("<h1>Welcome to my tiny twitter!</h1>")


def moments_input(request):
    if request.method == 'POST':
        form = MomentForm(request.POST)
        if form.is_valid():
            moment=form.save()
            moment.save()
            return HttpResponseRedirect(reverse("app.views.welcome"))
    else:
        form=MomentForm()
        PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return  render(request,os.path.join(PROJECT_ROOT,'app/templates','moments_input.html'),{'form':form})
