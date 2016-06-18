# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from calc.models import CalcTest
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

# Create your views here.


def testdb(request):
    saved_name = {"saved_name": "第一次用中文保存数据"}
    test1 = CalcTest(name=saved_name['saved_name'])
    test1.save()
    return render(request, "add.html", saved_name)
    # return HttpResponse("<p>数据成功保存至mysql</p>")


def get_testdb(request):
    fetch_all_list = CalcTest.objects.all()

    fetch_zh = CalcTest.objects.filter(name__contains="第一")

    fetch_en = CalcTest.objects.filter(name__contains="first")

    CalcTest.objects.order_by('id')

    # return render(request, "add.html", {"fetch_all_list": fetch_all_list})
    return render(request, "add.html", {"fetch_all_list": fetch_all_list, "fetch_zh": fetch_zh, "fetch_en": fetch_en})


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    request.encoding = "utf-8"
    if 'q' in request.GET:
        message = '你搜索的内容为：' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)


def search_post(request):
    ctx = {'tip': '你搜索的结果是： '}
    ctx.update(csrf(request))
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, 'post.html', ctx)


def post2(request):
    return render(request, 'post2.html')


def add(request):
    post2_rlt = {'add_result_tip': '计算结果是：'}
    post2_rlt.update(csrf(request))
    if request.POST:
        post2_rlt['add_result'] = str(int(request.POST['a'])+int(request.POST['b']))
    return render(request, 'post2.html', post2_rlt)
