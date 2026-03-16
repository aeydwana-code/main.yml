
import os
import requests

def get_crypto_prices():
    url = "https://api.coingecko.com/price?ids=bitcoin,ethereum,binancecoin&vs_currencies=usd"
    r = requests.get(url).json()
    btc, eth, bnb = r['bitcoin']['usd'], r['ethereum']['usd'], r['binancecoin']['usd']
    
    msg = (
        "⚡️ **المطور MP8 نظام صنعاء**\n"
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
    return requests.post(url, json=payload).status_code == 200

if __name__ == "__main__":
    content = get_crypto_prices()
    send_message(content)
