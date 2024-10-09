from urllib.request import urlopen  # 웹 페이지에 접속하기 위한 모듈

import requests
from bs4 import BeautifulSoup  # HTML 파싱을 위한 모듈

url = f'https://www.sempio.com/research/recipe/view/136'
# response = urlopen(url)
# soup = BeautifulSoup(response, 'html.parser')

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.text,'html.parser')

# title_list = soup.select('div',{'class':'subject'})

print(soup)