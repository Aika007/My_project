from django.db import models
from django.db.models.fields import EmailField


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя')
    last_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Фамилия')
    email = models.EmailField(unique=True, verbose_name='Почта')
    password = models.CharField(blank=True, null=True, max_length=500, verbose_name='Пароль')



