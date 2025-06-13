import os
import django
import sys 
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from decouple import config

# Set up Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from core.models import TelegramUser


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    TelegramUser.objects.get_or_create(
        username=user.username or '',
        chat_id=update.effective_chat.id,
        defaults={'first_name': user.first_name}
    )
    await update.message.reply_text(f"Hello, {user.first_name or 'user'}! Your username has been saved.")


def run_bot():
    token = config("TELEGRAM_BOT_TOKEN")
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Telegram bot is running...")
    app.run_polling()


if __name__ == "__main__":
    run_bot()
