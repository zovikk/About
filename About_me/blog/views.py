from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
# Create your views here.


def blog(request):
    news = Articles.objects.order_by('-date')
    return render(request, "blog/blogview.html", {'news': news})


def create(request):
    error = ''
    if request.method == "POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/blog')
        else:
            error = 'Форма заполнена неверно'

    form = ArticlesForm()

    data = {
        "form": form,
        "error": error,
    }

    return render(request, "blog/blogadd.html", data)
