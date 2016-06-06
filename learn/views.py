# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse(u"放射性废物管理")


def home(request):
    string_ = u"我正在学习用django编写一个放射性废物管理的网页"
    TutroialList = ['放射性废物',
                    '放射性',
                    '废物',
                    '管理']
    waste_info = {'type': u"固体废物", 'activity': "2E+10 Bq"}
    List = map(str, range(100))
    return render(request, 'home.html', {'string_': string_, 'TutorialList': TutroialList,
                                         'waste_info': waste_info,
                                         'List': List})


def add(request, a, b):
    c = int(a) + int(b)
    return render(request, 'home.html', {'c': c, 'a': a, 'b': b})


def definition_home(request):
    return render(request, r'definition\definition_home.html')
