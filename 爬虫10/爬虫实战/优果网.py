import requests
from bs4 import BeautifulSoup


a = requests.get('https://www.pengfu.com/content_1731983_1.html')
a.encoding = 'utf-8'

print(a.text)
soup = BeautifulSoup(a.text)
content = soup.select_one('.content-txt').get_text()
# href = soup.find_all('a',attrs={'class':'nslog'})

# pr
print(content)