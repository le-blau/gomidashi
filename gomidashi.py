import requests
import datetime
import os

def get_message():
    weekday = datetime.date.today().weekday()
    月, 火, 水, 木, 金, 土, 日 = range(7)

    week = {
        月:'なし',
        火:'古紙・ペット',
        水:'燃えるゴミ',
        木:'なし',
        金:'びん・カン・プラ',
        土:'なし',
        日:'燃えるゴミ'
    }
    return week[weekday]

def send():
    url = "https://notify-api.line.me/api/notify"
    access_token = os.environ['LINE_NOTIFY_TOKEN']
    headers = {'Authorization': 'Bearer ' + access_token}

    message = get_message()
    payload = {'message': message}
    r = requests.post(url, headers=headers, params=payload)

if __name__ == "__main__":
    send()