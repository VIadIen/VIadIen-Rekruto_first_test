from django.shortcuts import render
from django.http import HttpResponse


def rekruto(request):
    name = request.GET.get("name")
    message = request.GET.get("message")
    contex = f"<h3>Hello {name}!</h3><h3>{message}!</h3>"
    return HttpResponse(contex)