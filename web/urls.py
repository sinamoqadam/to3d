# from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='index'),
    path('^to3v', views.to3v, name='to3v'),
    path('^entrance_of_alighapou$', views.entrance_of_alighapou, name='entrance_of_alighapou'),
    path('^interior_of_alighapou$', views.interior_of_alighapou, name='interior_of_alighapou'),
    path('^interior_of_kashan_fin_garden$', views.interior_of_kashan_fin_garden, name='interior_of_kashan_fin_garden'),
    path('^fasham$', views.fasham, name='fasham'),
    path('^alighau$', views.alighau, name='alighau'),
    path('^kashan$', views.kashan, name='kashan'),
    path('^lavasan$', views.lavasan, name='lavasan'),
    path('^naghshe_jahan$', views.naghshe_jahan, name='naghshe_jahan'),
]