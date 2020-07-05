from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hello, world!")
    return render(request, "hello/index.html")

def nok(request):
    return HttpResponse("Hello, Nok!")


def greet(request, name: str):
    return render(request, "hello/greet.html", context={    "name": name.capitalize()    })
