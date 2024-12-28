from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    return HttpResponse("Hello from Django!")


def forums(request):
    context = {}
    return render(request, "forums/forums.html", context)
