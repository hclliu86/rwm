# -*- coding: UTF-8 -*-
# __author__ = 'liuhc'
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    return HttpResponse("hello world, how are you?")


def hello2(request):
    context = {"hello": "hello world from func(hello2)"}
    return render(request, 'hello.html', context)
