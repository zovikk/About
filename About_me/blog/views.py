from django.shortcuts import render, redirect
from .models import Articles, Like
# Create your views here.
from .forms import ArticlesForm


# def blog(request):
#     news = Articles.objects.order_by('-date')
#     return render(request, "blog/blogview.html", {'news': news})


def post_view(request):
    qs = Articles.objects.order_by('date')
    user = request.user

    context = {
        'qs': qs,
        'user': user,
    }

    return render(request, "blog/blogview.html", context)


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


def like_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post_obj = Articles.objects.get(id=post_id)

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post_id=post_id)

        if not created:
            if like.value == 'like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
    return redirect('blog:post-list')
