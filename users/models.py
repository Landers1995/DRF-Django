from django.db import models
from django.contrib.auth.models import AbstractUser
from materials.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.PositiveIntegerField(verbose_name='Телефон')
    city = models.CharField(max_length=50, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatars', verbose_name='Аватар', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
