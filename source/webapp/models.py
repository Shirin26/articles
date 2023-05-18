from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок')
    author = models.CharField(max_length=50, verbose_name='Автор', default='Unknown')
    content = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    def __str__(self):
        return f'{self.pk}: {self.title}'
