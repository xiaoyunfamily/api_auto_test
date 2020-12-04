import requests
from config.config import host
from demo.login.login import session

add_course_2_path = '/apijson/mgr/sq_mgr/'
add_course_2_url = host + add_course_2_path
headers = {'Content-Type': 'application/json'}
cookies = {'sessionid': session}
payload = {'action': 'add_course', 'data': '{"name": "初中化打动学d1", "desc": "初中化学课程", "display_idx": "4"}'}

res = requests.post(add_course_2_url, headers=headers, json=payload, cookies=cookies)
print(res.json())
