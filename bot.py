import os
import requests
import sys

def get_crypto_data():
    """جلب أسعار العملات الحقيقية من API عالمي"""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url, timeout=10)
        data = response.json()
        
        btc = data['bitcoin']['usd']
        btc_change = data['bitcoin']['usd_24h_change']
        eth = data['ethereum']['usd']
        bnb = data['binancecoin']['usd']
        
        msg = (
            "🔔 **تحديث نظام MP8 الذكي**\n"
            "━━━━━━━━━━━━━━━\n"
            f"₿ **Bitcoin:** ${btc:,.2f} ({btc_change:+.2f}%)\n"
            f"💎 **Ethereum:** ${eth:,.2f}\n"
            f"🔸 **BNB:** ${bnb:,.2f}\n"
            "━━━━━━━━━━━━━━━\n"
            "✅ النظام يعمل بكفاءة عالية"
        )
        return msg
    except Exception as e:
        return f"⚠️ خطأ في جلب البيانات: {str(e)}"

def send_to_telegram(text):
    """إرسال الرسالة مع فحص دقيق للأخطاء"""
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    
    if not token or not chat_id:
        print("❌ خطأ: لم يتم ضبط TELEGRAM_TOKEN أو TELEGRAM_CHAT_ID في Secrets")
        sys.exit(1)

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    
    try:
        r = requests.post(url, json=payload)
        result = r.json()
        if r.status_code == 200:
            print("🚀 تم الإرسال بنجاح إلى تليجرام!")
        else:
            print(f"❌ فشل الإرسال. رد تليجرام: {result.get('description')}")
            sys.exit(1)
    except Exception as e:
        print(f"❌ خطأ تقني: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    print("🔄 جاري تشغيل نظام MP8 المطور...")
    content = get_crypto_data()
    send_to_telegram(content)
