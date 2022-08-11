from django.shortcuts import render
# Create your views here.


def most(request):
    return render(request, "main/main.html")
