from venv import create

# Create your views here.
from django.urls import path

import women
from women import views
from women.views import about, contacts, questions

urlpatterns = [
    path("index/", views.WomenHome.as_view(), name="index"),
    path("about/", views.about, name="about"),
    path("contacts/", views.contacts, name="contacts"),
    path("questions/", views.questions, name="questions"),
    path("add-post/", views.add_women, name="add-post"),
    path("delete-post/<slug:women_slug>/", views.delete_women, name='delete-women'),
    path("detail-women/<slug:women_slug>/", views.detail_women, name='detail-women'),


]