import requests
from config.config import host
from demo.login.login import session

delete_course_path = '/api/mgr/sq_mgr/'
delete_course_url = host + delete_course_path
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookies = {'sessionid': session}
payload = {'action': 'delete_course', 'id': 2111}

res = requests.delete(delete_course_url, headers=headers, data=payload, cookies=cookies)
print(res.json())
