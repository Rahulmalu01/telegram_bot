from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json, requests, os
from .models import TelegramUser
from .tasks import send_welcome_email
from django.contrib.auth.models import User

@api_view(['GET'])
def public_view(request):
    return Response({"message": "This is a public endpoint."})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return Response({"message": f"Hello {request.user.username}, you're authenticated."})

@csrf_exempt
def telegram_webhook(request):
    data = json.loads(request.body)
    if "message" in data and data["message"]["text"] == "/start":
        username = data["message"]["from"].get("username", "")
        telegram_id = data["message"]["from"]["id"]
        TelegramUser.objects.update_or_create(
            telegram_id=telegram_id,
            defaults={"username": username}
        )
        requests.post(f"https://api.telegram.org/bot{os.getenv('TELEGRAM_BOT_TOKEN')}/sendMessage", data={
            "chat_id": telegram_id,
            "text": "You're now registered with our bot."
        })
    return JsonResponse({"ok": True})