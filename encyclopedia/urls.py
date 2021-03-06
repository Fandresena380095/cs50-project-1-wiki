from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path('wiki/<str:page>', views.entry_page , name= "entry_page"),
    path("wiki/create/" , views.create , name = "create"),
    path("wiki/<str:p_title>/edit_page/" , views.edit , name = "edit"),
    path("random/", views.random , name="random")

]
