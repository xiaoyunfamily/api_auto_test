import requests


def get_session():
    host = 'http://localhost'
    login_path = '/api/mgr/loginReq'
    login_url = host + login_path
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'username': 'auto', 'password': 'sdfsdfsdf'}
    res = requests.post(login_url, headers=headers, data=payload)
    session = res.cookies['sessionid']
    return session


if __name__ == '__main__':
    session = get_session()
    print(session)
