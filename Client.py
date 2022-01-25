# t0 -> pegar tempo atual do computador e descontar tempo aleatório
# t1 e t2 -> obter tempo atual do servidor
# t3 -> adicionar 5 segundos ao t0

# Imprimir tempo de defasage me horario ajustado

import json
import random
import requests
from datetime import datetime, timedelta


seconds_to_subtract = random.randint(3, 5)
format = '%Y-%m-%d %H:%M:%S'

time_dict = {
    'time_0': (datetime.now() - timedelta(seconds=seconds_to_subtract)).strftime(format)
}

response = requests.get('http://127.0.0.1:8000', json=time_dict)
time_dict = json.loads(response.content.decode())


for index, time_key in enumerate(time_dict):
    splited_date, splited_time = time_dict[time_key].split(' ')

    year, month, day = splited_date.split('-')
    hour, minute, second = splited_time.split(':')

    time_dict[time_key] = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
    print(f'Time[{index}]: {time_dict[time_key].strftime("%H:%M:%S")}')


time_dict['time_3'] = time_dict['time_0'] + timedelta(seconds=5)

lag_time = (
    (time_dict['time_1'] - time_dict['time_0']) + (time_dict['time_2'] - time_dict['time_3'])
) / 2

time_synchronized = time_dict['time_3'] + timedelta(seconds=lag_time.seconds)

print(f'Defasagem => {lag_time}')
print(f'Horário Ajustado => {time_synchronized.strftime("%H:%M:%S")}')
