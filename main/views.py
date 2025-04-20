from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    data = {"title": "Index HTML", "content": "Hello from index.html"}
    return render(request, "main/index.html", data)


def about(request):
    return HttpResponse("About page")
