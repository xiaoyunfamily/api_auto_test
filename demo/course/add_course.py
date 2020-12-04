import requests
from config.config import host
from demo.login.login import session

add_course_path = '/api/mgr/sq_mgr/'
add_course_url = host + add_course_path
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookies = {'sessionid': session}
payload = {'action': 'add_course', 'data': '{"name": "初中化打动学1", "desc": "初中化学课程", "display_idx": "4"}'}
print(payload)

res = requests.post(add_course_url, headers=headers, data=payload, cookies=cookies)
print(res.json())
