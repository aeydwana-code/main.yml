
import os
import requests

def send_test():
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    msg = "🚀 النظام يعمل بنجاح! تم الربط مع MP8"
    url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    r = requests.get(url)
    print(r.json())

if __name__ == "__main__":
    send_test()
