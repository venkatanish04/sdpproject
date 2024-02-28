import email
import random
import string
from django.shortcuts import *

from .forms import *
from django.http import HttpResponse
import datetime
from .models import *
def hello1(request):
    return HttpResponse("<center>Welcome To Travel Management HomePage</center>")

def newhomepage(request):
    return render(request,'NewHome.html')

def travelpackage(request):
    return render(request,'TravelPackage.html')
def print1(request):
    return render(request,'print_to_console.html')

def print_to_console(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'user input: {user_input}')
        a1 = {'user_input': user_input}
        return render(request, 'print_to_console.html',a1)

def randomcall(request):
    return render(request, 'randomgenerator.html')

def randomlogic(request):
    if request.method == "POST":
        user_input = request.POST['user_input']
        print(f'user input: {user_input}')
        a2 = int(user_input)
        ran1 = ''.join(random.sample(string.digits, k=a2))

        a1 = {'ran1': ran1}
        return render(request, 'randomgenerator.html', a1)

def getdate1(request):
    return render(request,'Getdate.html')

from django.shortcuts import render
def getdate(request):
    if request.method == 'POST':
        form = IntegerDateForm(request.POST)
        if form.is_valid():
            integer_value = form.cleaned_data['integer_value']
            date_value = form.cleaned_data['date_value']
            updated_date = date_value + datetime.timedelta(days=integer_value)
            return render(request, 'Getdate.html', {'updated_date': updated_date})
    else:
        form = IntegerDateForm()

    return render(request, 'Getdate.html', {'form': form})
def registercall(request):
    return render(request,'Register.html')

def registerlogin(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        phonenumber=request.POST.get('phonenumber')

        if Anish.objects.filter(email=email).exists():
            return HttpResponse("Email is already Registered Please try with another Email")

        Anish.objects.create(name=name,email=email,password=password,phonenumber=phonenumber)
        return redirect('NewHome')
    return render(request,'Register.html')





def pie_chart(request):
    return render(request,'chart_form.html')
import matplotlib.pyplot as plt
import numpy as np




def pie_chart(request):
    if request.method == 'POST':
        form = PieChartForm(request.POST)
        if form.is_valid():
            # Process user input
            y_values = [int(val) for val in form.cleaned_data['y_values'].split(',')]
            labels = [label.strip() for label in form.cleaned_data['labels'].split(',')]

            # Create pie chart
            plt.pie(y_values, labels=labels, startangle=90)
            plt.savefig('static/images/pie_chart.png')  # Save the chart image
            img1={'chart_image': '/static/images/pie_chart.png'}
            return render(request, 'chart_form.html', img1)
    else:
        form = PieChartForm()
    return render(request, 'chart_form.html', {'form': form})

def callcar(request):
    return render(request, 'Cards.html')
import requests

def callweather (request):
    return render(request, 'weatherappinput.html')
def weatherlogic(request):
    if request.method == 'POST':
        place = request.POST['place']
        API_KEY = '77c738948cf452ab2e2b1256148cee41'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={place}&appid={API_KEY}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            temperature1= round(temperature - 273.15,2)
            return render(request, 'weatherappinput.html',
                          {'city': str.upper(place), 'temperature1': temperature1, 'humidity': humidity})
        else:
            error_message = 'City not found. Please try again.'
            return render(request, 'weatherappinput.html', {'error_message': error_message})

from django.core.mail import send_mail
from .models import Feedback
def feedback(request):
    return render(request,'feedbackform.html')


def mainfeedback(request):
    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        Email = request.POST.get('Email')
        Comment = request.POST.get('Comment')
        tosend = Comment + ' Thankyou'
        Feedback.objects.create(FirstName=FirstName, LastName=LastName, Email=Email, Comment=Comment)
        send_mail(
            'Thank You for contacting anish travels tourism and manage',  # <- Added comma here
            tosend,
            '2200032220cseh@gmail.com',
            [Email],
            fail_silently=False,
        )

        return redirect('NewHome')
    # This line should be indented inside the if block

    return render(request, 'feedbackform.html')


from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'Login.html')


def signup(request):
    return render(request, 'Signup.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = auth.authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            return render(request, 'NewHome.html')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'Login.html')
    else:
        return render(request, 'Login.html')


def signup1(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Usename already taken')
                return render(request, 'Signup.html')
            else:
                user = User.objects.create_user(username=username, password=pass1)
                user.save()
                messages.info(request, 'Account created successfully!!')
                return render(request, 'Login.html')
        else:
            messages.info(request, 'Password do not match')
            return render(request, 'Signup.html')

