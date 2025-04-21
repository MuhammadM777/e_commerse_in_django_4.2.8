from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    data = {"title": "Main Page", "content": "Магазин мебели HOME"}
    return render(request, "main/index.html", data)


def about(request):
    data = {
        "title": "Main Page", 
        "content": "Магазин мебели HOME",
        "text_on_page": "teks bu magazyn hakynda bu nahili gowy magazyn"
    }
    return render(request, 'main/about.html', data)
