import requests

url = 'http://localhost:8050/render.html?url=http://www.baidu.com'

response = requests.get(url)

print(response.text)