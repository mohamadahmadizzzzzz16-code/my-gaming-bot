import telebot # یا کتابخانه‌ای که استفاده می‌کنید

# 1. تنظیم Flask برای اینکه Render را راضی نگه دارد
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# 2. کد اصلی ربات شما
def run_bot():
    # اینجا همان کد اصلی ربات خود را بگذارید
    # مثلا: bot.polling(none_stop=True)
    pass

# 3. اجرای همزمان (Multi-threading)
if __name__ == "__main__":
    # اجرای ربات در پس‌زمینه
    Thread(target=run_bot).start()
    # اجرای سرور وب در کانتینر اصلی
    app.run(host='0.0.0.0', port=5000)
 os
import json
import requests
import feedparser
from flask import Flask

app = Flask(__name__)

# برای امنیت، توکن را از متغیر محیطی می‌خوانیم
BOT_TOKEN = ("8735821967:AAHipO565_SZyXXGBLdLPHfH_hD7VKUuzfA")
DESTINATIONS = ["@MajorCurrencies1", "-100893455426"]
RSS_FEED_URL = "https://www.zoomg.ir/feed/" # فید زومجی
HISTORY_FILE = "sent_links_gaming.json"

def load_sent_links():
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except: return []
    return []

def save_sent_links(links):
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(links, f, ensure_ascii=False)

def send_telegram_message(chat_id, text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text, "parse_mode": "HTML"}
    try:
        requests.post(url, json=payload, timeout=10)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
@app.route('/run')
def check_and_send():
    sent_links = load_sent_links()
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(RSS_FEED_URL, headers=headers, timeout=10)
        feed = feedparser.parse(response.text)
        if not feed.entries: return "Feed empty", 500
        for entry in reversed(feed.entries[:3]):
            if entry.link not in sent_links:
                msg = f"<b>{entry.title}</b>\n\n{entry.link}"
                for chat_id in DESTINATIONS:
                    send_telegram_message(chat_id, msg)
                sent_links.append(entry.link)
        save_sent_links(sent_links)
        return "Bot checked and sent successfully!"
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run()
if __name__ == "__main__":
    # اجرای ربات در یک رشته (Thread) جداگانه
    Thread(target=run_bot).start()
    # اجرای سرور وب برای راضی نگه داشتن Render
    app.run(host='0.0.0.0', port=5000)
