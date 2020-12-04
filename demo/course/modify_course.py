import requests
from config.config import host
from demo.login.login import session

modify_course_path = '/api/mgr/sq_mgr/'
modify_course_url = host + modify_course_path
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookies = {'sessionid': session}
payload = {'action': 'modify_course', 'id': 2112,
           'newdata': '{"name": "初中化打动学1", "desc": "初中化学000课程", "display_idx": "4"}'}

res = requests.put(modify_course_url, headers=headers, data=payload, cookies=cookies)
print(res.json())
