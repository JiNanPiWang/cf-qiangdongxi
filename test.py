import requests
import chardet

url = "https://cf.qq.com"
cookie = {"session_id": "<your_login_session_id>"}

response = requests.get(url, cookies=cookie)
encoding = chardet.detect(response.content)['encoding']
print(response.content.decode(encoding))
