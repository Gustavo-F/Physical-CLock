import json
import socket
import random
import threading
from time import sleep
from datetime import datetime

def worker_thread(client_socket):
    data = client_socket.recv(1024)
    data = data.decode().split('\r\n')[-1]

    status_code = '200 OK'
    format = '%Y-%m-%d %H:%M:%S'

    try:
        time_dict = {
            'time_0': json.loads(data)['time_0'],
            'time_1': datetime.now().strftime(format),
        }

        sleep(random.randint(5, 15))
        time_dict['time_2'] = datetime.now().strftime(format)
        
        response_data = json.dumps(time_dict)
    except:
        status_code = '400 Bad Request'
        response_data = json.dumps({'message': 'Error!'})

    try:
        response = (
            f'HTTP/1.1 {status_code}\n'
            f'Content-Type: application/json\n\n'
            f'{response_data}'
        ).encode()

        client_socket.send(response)
    except:
        print('Coul not send reply.')

    client_socket.shutdown(socket.SHUT_RDWR)    

def Main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    server_socket.bind(('127.0.0.1', 8000)) 
    
    server_socket.listen() 
    print('Server initialized...')
    
    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Client connected: {client_address[0]}:{client_address[1]}')

        threading.Thread(target=worker_thread, args=[client_socket]).start()


if __name__ == '__main__':
    Main()
