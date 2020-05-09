from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def home_view(request):
    template = loader.get_template('web/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def test(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def test2(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def test3(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def test4(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))
