
name: MP8 Crypto Tracker
on:
  workflow_dispatch:
  schedule:
    - cron: '0 * * * *' # يعمل تلقائياً كل ساعة

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: pip install requests

      - name: Run Crypto Bot
        env:
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
        run: |
          import os
          import requests
          
          def send_msg():
              token = os.getenv("TELEGRAM_TOKEN")
              chat_id = os.getenv("TELEGRAM_CHAT_ID")
              
              # جلب الأسعار
              url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
              data = requests.get(url).json()
              
              btc = data['bitcoin']['usd']
              eth = data['ethereum']['usd']
              sol = data['solana']['usd']
              
              text = f"🚀 **نظام صنعاء MP8**\n\n🧡 Bitcoin: ${btc:,}\n💙 Ethereum: ${eth:,}\n💜 Solana: ${sol:,}"
              
              send_url = f"https://api.telegram.org/bot{token}/sendMessage"
              requests.post(send_url, json={"chat_id": chat_id, "text": text, "parse_mode": "Markdown"})
          
          if __name__ == "__main__":
              send_msg()
        shell: python
