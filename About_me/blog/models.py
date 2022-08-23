from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Articles(models.Model):

    title = models.CharField('Название', max_length=50, default='')
    full_text = models.TextField('Статья')
    liked = models.ManyToManyField(User, default=None, blank=True, related_name="liked")
    date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="author")

    def __str__(self):   # служит для вывода информации каждого отдельного объекта
        return self.title

    @ property
    def num_likes(self):
        return self.liked.all().count()

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Articles, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def __str__(self):
        return str(self.post)
