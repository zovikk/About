from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):   # служит для вывода информации каждого отдельного объекта
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
