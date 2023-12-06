from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
    #return HttpResponse('homepage')
    return render(request,"homepage.html")

def about(request):
    return render(request,"about.html")

    #return HttpResponse('about')

def criterias(request):
    return render(request,'criteria.html')
