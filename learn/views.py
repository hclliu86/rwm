# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"放射性废物管理")


def home(request):
    string_ = u"我正在学习用django编写一个放射性废物管理的网页"
    return render(request, 'home.html', {'string_': string_})