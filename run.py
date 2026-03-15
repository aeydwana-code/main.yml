
import requests
import os

# إعدادات الأمان
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
USER = "aeydwana-code"

# قائمة الأهداف (المستودعات التي استخرجناها من صورتك)
TARGETS = [
    "cryptography.fernet",
    "cryptography.fer",
    "comboclean" # أضفت هذا بناءً على وصف أحد مستودعاتك
]

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})

def scan_repositories():
    send_msg(f"🚀 **بدء عملية اقتناص الملفات من المستودعات المستهدفة...**")
    
    for repo in TARGETS:
        api_url = f"https://api.github.com/repos/{USER}/{repo}/contents"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            files = response.json()
            for file in files:
                # سحب أي ملف ينتهي بـ .txt (ملفات الـ Combo عادة تكون هكذا)
                if file['name'].endswith('.txt'):
                    raw_url = file['download_url']
                    info = f"📂 **مستودع:** `{repo}`\n📄 **ملف:** `{file['name']}`\n🔗 [اضغط هنا لتحميل الملف]({raw_url})"
                    send_msg(info)
        else:
            send_msg(f"⚠️ تعذر فحص المستودع: `{repo}`")

if __name__ == "__main__":
    scan_repositories()
