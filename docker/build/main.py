import requests


def check_request():
    resp = requests.get('https://docs.docker.com')
    print(resp)


if __name__ == '__main__':
    check_request()