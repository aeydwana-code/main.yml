
import os
import requests

def get_crypto_prices():
    # جلب أسعار العملات الحقيقية
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd"
    response = requests.get(url).json()
    
    btc = response['bitcoin']['usd']
    eth = response['ethereum']['usd']
    bnb = response['binancecoin']['usd']
    
    msg = (
        "⚡️ **نظام صنعاء MP8 المطور**\n"
        "━━━━━━━━━━━━━━━\n"
        f"💰 **BTC:** ${btc:,.0f}\n"
        f"💎 **ETH:** ${eth:,.2f}\n"
        f"🔸 **BNB:** ${bnb:,.2f}\n"
        "━━━━━━━━━━━━━━━\n"
        "✅ تم التحديث بنجاح من GitHub"
    )
    return msg

def send_message(text):
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('TELEGRAM_CHAT_ID')
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
    r = requests.post(url, json=payload)
    return r.status_code == 200

if __name__ == "__main__":
    try:
        content = get_crypto_prices()
        if send_message(content):
            print("🚀 Success: Message sent to CryptoSanaaBot!")
        else:
            print("❌ Failure: Check Token and Chat ID.")
    except Exception as e:
        print(f"⚠️ Error: {e}")
