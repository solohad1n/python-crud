from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Note(models.Model):
    name = models.CharField('Название' ,max_length=150)
    description = models.TextField('Описание')
    created_at = models.DateField('Дата создания', auto_now_add=True)
    file = models.FileField('Доп. файл', upload_to='notes', blank=True, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')

    class Meta:
        verbose_name = "заметку"
        verbose_name_plural = "Заметки"

    def __str__(self):
        return self.name + ' - ' + self.description