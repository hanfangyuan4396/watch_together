import time
import threading
import datetime
import requests
from wechat_api import wechat_api

def add_time(s):
    return f"{datetime.datetime.now().strftime('%m-%d %H:%M:%S')} {s}"

def delete_item(data):
    length = len(data)
    if 0 < length < 5:
        expiration_time = 24 * 3 # 房间号有效期3天
    elif 5 <= length < 10:
        expiration_time = 24 # 1天
    elif 10 <= length < 100:
        expiration_time = 2 # 2小时
    else:
        expiration_time = 0.01 # 36秒
    delete_list = []
    now = time.time() * 1000
    for key, value in data.items():
        if value['timestamp'] < now - 1000 * 60 * 60 * expiration_time:
            delete_list.append(key)
    for item in delete_list:
        del data[item]
    # 查询房间号信息发送给微信
    text = '\n'
    print(len(data))
    for key, value in data.items():
        text += f'room_id:{key} current_time:{value["current_time"]}\n'
        print(text)
        
    try:
        print(add_time(text))
        wechat_api.send_text_message('info', add_time(text))
    except:
        print(add_time('发送到微信失败'))


def website_clear_supervisor():
    while True:
        url = 'http://49.232.11.80/api/clear'
        data = {'password': 'hanfangyuan'}
        response = requests.post(url, json=data)
        if response.status_code == 200:
            text = response.json()['message']
            wechat_api.send_text_message('info', f'website works normally\n{text}')
        else:
            wechat_api.send_text_message('error', 'website is abnormal')
        time.sleep(60 * 60 * 24)

website_clear_supervisor_thread = threading.Thread(target=website_clear_supervisor)

if __name__=='__main__':
    # data = {}
    # import random
    # for i in range(200):
    #     data[i] = {'current_time': 1, 'timestamp': (time.time()+ random.randint(0, 20)) * 1000}
    # delete_item_thread = threading.Thread(target=delete_item, args=(data,))
    # delete_item_thread.start()
    website_clear_supervisor()
