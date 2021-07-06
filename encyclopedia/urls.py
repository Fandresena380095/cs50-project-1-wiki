from django.urls import path

from . import views

urlpatterns = [
    path("wiki/", views.index, name="index"),
    path('wiki/<str:page>', views.entry_page , name= "entry_page"),
    path("wiki/create/" , views.create , name = "create")
]
