import requests, os

token = os.getenv('TELEGRAM_TOKEN')
chat_id = os.getenv('TELEGRAM_CHAT_ID')

def launch():
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": "🎯 نظام MP8: تم الاتصال بنجاح! الأسطول جاهز."}
    requests.post(url, json=payload)

if __name__ == "__main__":
    launch()

