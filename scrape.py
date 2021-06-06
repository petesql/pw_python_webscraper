import requests

res = requests.get('https://peter-whyte.com')
txt = res.text
status = res.status_code

print(txt, status)