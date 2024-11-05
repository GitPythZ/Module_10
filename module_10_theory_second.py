from threading import Thread
import requests
from datetime import datetime

time_start = datetime.now()
THE_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre/'
res = []


def func(url):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)


thr_first = Thread(target=func, args=(THE_URL,))
thr_second = Thread(target=func, args=(THE_URL,))
thr_third = Thread(target=func, args=(THE_URL,))

thr_first.start()
thr_second.start()
thr_third.start()

thr_first.join()
thr_second.join()
thr_third.join()

time_end = datetime.now()
time_res = time_end - time_start
print(time_res)
print(res)
