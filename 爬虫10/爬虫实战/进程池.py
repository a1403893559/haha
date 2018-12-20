from  concurrent.futures import ThreadPoolExecutor
import time
import threading
import requests
pool  = ThreadPoolExecutor(10)

def get_data(url):
    print(url)
    print('开始下载')
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36'
    }
    response = requests.get('https://www.baidu.com', headers=headers)
    print(response.text)
    return response.text,url
def done(future):
    print('下载完了')
    response  = future.result()
    print(response)
urls = [
'https://www.baidu.com',
'https://www.baidu.com',
]


for url in urls:
    handle = pool.submit(get_data,(url,))
    handle.add_done_callback(done)

print(threading.current_thread().name)
pool.shutdown(True)
