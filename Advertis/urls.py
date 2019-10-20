from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path("add-adv/",views.add_adv,name="add_adv"),
    path("my_advertises/",views.my_advertises,name="my_advertises"),
    path("view-adv/",views.view_adv,name="view_adv"),
    url(r'^view-adv/(?P<adv_id>[0-9]*)$',views.adv_details,name="adv_details"),
    url(r'^my_advertises/edit/(?P<adv_id>[0-9]*)$',views.edit_adv,name="edit_adv"),
    url(r'^my_advertises/delete/(?P<adv_id>[0-9]*)$',views.delete_adv,name="delete_adv"),




]