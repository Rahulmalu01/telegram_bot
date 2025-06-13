from django.urls import path
from .views import public_view, protected_view, telegram_webhook

urlpatterns = [
    path('public/', public_view),
    path('protected/', protected_view),
    path('telegram-webhook/', telegram_webhook),
]