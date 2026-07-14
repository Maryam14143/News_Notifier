import feedparser
import requests
import time

url = "https://www.varzesh3.com/rss/all"
keyword = ["فوتبال","والیبال","نکواندو"]
history = []

def check_website(url):
    feed = feedparser.parse(url)
    try:
        for entry in feed.entries:
            for word in keyword:
                if word in entry.title:
                    if entry.title not in history:
                        history.append(entry.title)
                        return entry
        return None
    except Exception as e:
        print("خطا در جستجو در سایت")
        return None

TOKEN = "YOUR_TOKEN_HERE"
CHAT_ID = "YOUR_CHAT_ID_HERE"

def send_bale(New_News):
    if New_News is None:
        return 0
    url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"
    message = f"خبرهای جدید : {New_News.title}\n{New_News.link}"
    payload = {'chat_id': CHAT_ID, 'text': message}
    try:
        requests.post(url, json=payload, timeout=20)
        print("به بله ارسال شد")
    except Exception as e:
        print("خطا در ارسال به بله")

while True:
    News = check_website(url)
    if News is not None:
        send_bale(News)

    time.sleep(1800)