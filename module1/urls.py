from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('hello1/', hello1, name='hello1'),
    path('',newhomepage, name='NewHome'),
    path('travel/',travelpackage, name="TravelPackage"),
    path('user_input', print_to_console, name="print_to_console"),
    path('print1/', print1 , name='print1'),
    path('randomcall/',randomcall,name='randomcall'),
    path('randomlogic/', randomlogic, name='randomlogic'),
    path('getdate/',getdate1,name='getdate1'),
    path('getmain/',getdate,name='getmain'),
    path('register/',registercall,name='registercall'),
    path('registerlogin/',registerlogin,name='registerlogin'),
    path('piechart/', pie_chart, name='pie_chart'),
    path('car/',callcar,name='car'),
    path('callweather/',callweather,name='callweather'),
    path('weatherlogic/', weatherlogic, name='weatherlogic'),
    path('Feedback/', Feedback, name='Feedback'),
    path('mainfeedback/', mainfeedback, name='mainfeedback'),
    path('login/',login,name='login'),
    path('login1/',login1,name='login1'),

    path('signup/',signup,name='signup'),
    path('signup1/',signup1,name='signup1'),

]