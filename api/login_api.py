import requests
from config import host
from lib.excel_lib import ExcelLib

login_api_row = 1
msg_list = ExcelLib().get_api_msg_list(login_api_row)
print(type(msg_list))

def login(username, password):
    login_path = msg_list[0]
    login_url = host + login_path
    headers = msg_list[2]

    payload = {'username': username, 'password': password}
    res = requests.post(login_url, headers=headers, data=payload)
    return res.json()


if __name__ == '__main__':
    print(login('auto', 'sdfsdfsdf'))
