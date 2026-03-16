import os
import requests

token = os.getenv("TELEGRAM_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

msg = "🚀 البوت يعمل بنجاح عبر GitHub Actions"

url = f"https://api.telegram.org/bot{token}/sendMessage"

data = {
    "chat_id": chat_id,
    "text": msg
}

requests.post(url, data=data)
