import requests
from config.config import host
from demo.login.login import session

list_course_path = '/api/mgr/sq_mgr/'
list_course_url = host + list_course_path
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
cookies = {'sessionid': session}
payload = {'action': 'list_course', 'pagenum': '1', 'pagesize': '20'}

res = requests.get(list_course_url, payload, headers=headers, cookies=cookies)
print(res.json())
