import json
import random
import requests
from datetime import datetime, timedelta

seconds_to_subtract = random.randint(5, 10)
wrong_time = (datetime.now() - timedelta(seconds=seconds_to_subtract)).time().strftime('%H:%M:%S')

time_dict = {
    'time_0': wrong_time
}

response = requests.get('http://127.0.0.1:8080')