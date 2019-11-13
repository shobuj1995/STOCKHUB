from django.shortcuts import render, redirect

from  django.shortcuts import HttpResponse

from .models import News
from .forms import RegistrationForm
from .models import RegistrationData
from django.contrib import messages
def home(request):
    context={"text":"this is from context"}
    return render(request,"home.html",context)

def contact(request):
    context = {
        "fruits":["apple","Banana","pear","melon"]

    }
    return render(request, "contact.html", context)


def about(request):
    context = {}
    return render(request, "about.html", context)

def news_details(request):
    obj = News.objects.get(id=2)
    context = {
        "object":obj
    }
    return render(request, "news_details.html", context)

def news_year(request, year):
    a_list = News.objects.filter(pub_date__year = year)
    context = {
        'year':year,
        'article_list':a_list
    }
    return render(request, "news_year.html", context)

def register(request):
    context = {"form":RegistrationForm}
    return render(request, "registration.html", context)
	
	
def login_action(request):
	return HttpResponse(1)


def advise(request):
    context = {}
    return render(request, "advisor.html", context)
def learn(request):
    context = {}
    return render(request, "learn.html", context)


def predict(request):
    context = {}
    return render(request, "predictor.html", context)

def addUser(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        register=RegistrationData(username = form.cleaned_data['username'],
                                  password=form.cleaned_data['password'],
                                  email=form.cleaned_data['email'],
                                  phone=form.cleaned_data['phone'])
        register.save()

        messages.add_message(request, messages.SUCCESS, "Your Registration is successful")

    return  redirect('add')

# Create your views here.
