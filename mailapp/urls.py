from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('',send_emails,name='send_emails'),

]