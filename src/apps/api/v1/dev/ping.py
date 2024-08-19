import requests
import time
from config.settings import SERVER_DOMAIN

def ping_server():
    while True:
        try:
            response = requests.get(f'http://{SERVER_DOMAIN}/api/dev/ping/')
            print(f'Ping response status code: {response.status_code}')
        except Exception as e:
            print(f'Error pinging server: {e}')
        

        time.sleep(300)  # 5 минут
      