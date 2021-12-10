import json
import random
import requests
from datetime import datetime, timedelta, time

seconds_to_subtract = random.randint(5, 10)
wrong_time = (datetime.now() - timedelta(seconds=seconds_to_subtract)).time().strftime('%H:%M:%S')

time_dict = {
    'time_0': wrong_time
}

response = requests.get('http://127.0.0.1:8000', json=time_dict)

time_dict = json.loads(response.content.decode())
time_dict['time_03'] = datetime.now().strftime('%H:%M:%S')

for time_key in time_dict:
    hour, minute, second = time_dict[time_key].split(':')
    time_dict[time_key] = time(int(hour), int(minute), int(second))
    
sync_time = datetime.combine((time_dict['time_1'] - time_dict['time_0']) + (time_dict['time_2'] - time_dict['time_3']))
print(f'Sync Time => {sync_time}')
