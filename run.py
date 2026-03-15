
import requests
import os
from datetime import datetime, timedelta

# إعدادات الأمان
TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')
USER = "aeydwana-code"

# قائمة الأهداف الكاملة (المستودعات الـ 13)
TARGETS = [
    "cryptography.fernet",
    "cryptography.fer",
    "comboclean",
    "main.yml",
    # أضف بقية أسماء مستودعاتك هنا بين علامات التنصيص
]

def send_msg(text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": text, "parse_mode": "Markdown"})

def scan_and_filter():
    send_msg("📡 **بدء المسح الذكي (نظام MP8)**\n🔍 جاري البحث عن ملفات Combo جديدة...")
    
    found_new = False
    # تحديد وقت الفلتر (آخر 24 ساعة مثلاً)
    time_limit = datetime.now() - timedelta(days=1)

    for repo in TARGETS:
        api_url = f"https://api.github.com/repos/{USER}/{repo}/contents"
        response = requests.get(api_url)
        
        if response.status_code == 200:
            files = response.json()
            for file in files:
                # فلتر: ملفات نصية فقط
                if file['name'].endswith('.txt'):
                    # فلتر ذكي: جلب روابط التحميل المباشرة
                    raw_url = file['download_url']
                    
                    # إرسال البيانات فوراً
                    info = f"🎯 **صيد جديد!**\n📂 مستودع: `{repo}`\n📄 ملف: `{file['name']}`\n🔗 [تحميل الملف المباشر]({raw_url})"
                    send_msg(info)
                    found_new = True
        
    if not found_new:
        send_msg("📭 لا توجد ملفات نصية جديدة في المستودعات حالياً.")

if __name__ == "__main__":
    if TOKEN and CHAT_ID:
        scan_and_filter()
    else:
        print("Configuration Error!")
