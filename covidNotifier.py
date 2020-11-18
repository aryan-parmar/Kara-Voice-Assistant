from plyer import notification
import requests
from bs4 import BeautifulSoup


def notifyme(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon=r"winlogo.ico",
        timeout=10
    )


def getData():
    req = requests.get('https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data/India_medical_cases_chart')
    data = req.text
    soup = BeautifulSoup(data, 'html.parser')
    b = soup.find_all("tbody")[0].find_all("tr")[-2]
    d = b.find_all("td")
    notifyme("hello sir", f"todays cases in india are:-   {d[-2].getText()}")

