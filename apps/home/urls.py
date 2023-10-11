from django.urls import path, re_path
from apps.home import views

urlpatterns = [
    # The home page
    path('', views.index, name='home'),
    path('', views.forms, name='forms'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
