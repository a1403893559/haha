import requests

url = 'https://www.qisuu.la/du/7/7310/8725877.html'

a =requests.get(url)
print(a.text)