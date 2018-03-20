import requests
from json import dumps

def main():
    url = 'https://chat.googleapis.com/v1/spaces/AAAAVSsxN8I/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=0hEkgEiw7cTbQNFiEOWBf5lcRHZKm3SxIQqopjK4aHM%3D'
    bot_message = {
        'text' : 'Hello from Python script!'}

    message_headers = { 'Content-Type': 'application/json; charset=UTF-8'}

    # http_obj = Http()

    response = requests.post(
        url=url,
        headers=message_headers,
        data=dumps(bot_message),
    )

    print(response.text)

if __name__ == '__main__':
    main()
