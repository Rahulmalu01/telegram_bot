from django.db import models
from django.contrib.auth.models import User

class TelegramUser(models.Model):
    username = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
