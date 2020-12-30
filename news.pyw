import requests
from plyer import notification
import schedule
import time
def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=6,
        ticker='Kara'
    )

def news():
    url = 'https://newsapi.org/v2/top-headlines?sources=google-news&apiKey=8dbbb63e883a49a68d03432385a7a06e'
    response = requests.get(url)
    a = response.json()
    notifyme("Kara news", a.get("articles")[0].get('title'))

schedule.every(30).minutes.do(news)
while True:
    schedule.run_pending()
    time.sleep(1)