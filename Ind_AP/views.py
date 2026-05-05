from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def chittoor(request) :
        response = "<h1> Welcome to Chittoor</h1>"
        return render(request, "chittoor.html")


def Kadapa(request) :
        response = "<h1> Welcome to Kadapa</h1>"
        return HttpResponse(response)