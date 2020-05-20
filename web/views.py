from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def home_view(request):
    template = loader.get_template('web/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def to3v(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def entrance_of_alighapou(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def interior_of_alighapou(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def interior_of_kashan_fin_garden(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def fasham(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def alighau(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def kashan(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def lavasan(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))


def naghshe_jahan(request):
    template = loader.get_template('web/test.html')
    context = {}
    return HttpResponse(template.render(context, request))
