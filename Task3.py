import requests
from pprint import pprint 
from datetime import *
import time

def get_json(url,page):
    fromday = date.today() - timedelta(days=2)
    fromdate = round(time.mktime(fromday.timetuple()))
    params = {
        'tagged': 'Python',
        'site': 'stackoverflow',
        'fromdate': str(fromdate),
        'page' : page
        }
    response = requests.get(url = url, params=params)
    return response.json()


def python_questions(url, page=1):
    data = get_json(url, page)
    items = data['items']
    for item in items:
        print(f"Вопрос №: {item['question_id']}")
        print(f"\tЗаголовок: {item['title']}")
        print(f"\tСсылка: {item['link']}")
        print("\tТеги:", end=" ")
        for tag in item['tags']:
            if tag != item['tags'][-1]:
                print(tag, end=", ")
            else: 
                print(tag)
        date = datetime.fromtimestamp(item['creation_date']) 
        print(f"\tДата создания вопроса: {date}")
        
    if data['has_more'] == True:
        page += 1
        data = get_json(url, page)
        if 'error_id' in data:
            print(data['error_message'])
            return 0
        python_questions(url, page)
    

url = 'https://api.stackexchange.com/2.3/questions'
python_questions(url) # 1 (start_page)