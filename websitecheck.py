## COMO CHECAR SE UM SITE ESTAR ONLINE ##

import requests



def get_status (url: str) -> int:
    request = requests.get(url)
    return request.status_code



if __name__ == '__main__':
    print(get_status('https://www.apple.com.br'))
    print('O Site está online.')

