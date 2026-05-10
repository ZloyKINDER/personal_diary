from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_ckeditor_5.fields import CKEditor5Field

class Entry(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    content = CKEditor5Field('Содержание', config_name='default')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='entries')

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('entry_detail', kwargs={'pk': self.pk})