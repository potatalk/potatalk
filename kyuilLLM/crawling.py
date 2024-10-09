import csv  # CSV 파일을 다루기 위한 모듈
from urllib.request import urlopen  # 웹 페이지에 접속하기 위한 모듈

import requests
from bs4 import BeautifulSoup  # HTML 파싱을 위한 모듈
import pandas as pd

test_list = []
category = ''
for number in range(1, 3300):

    url = 'https://ifs.menupan.com/mws/cook/onepage/onepage.asp?id='+str(number)+'&recode=theme&code=60&r_pg=1&cookierecipe='
    response = urlopen(url)
    soup = BeautifulSoup(response, 'html.parser')

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}
    res = requests.get('URL', headers=headers)


    title_list = soup.select('div',{'class':'subject'})

    print(title_list)
#     if title_list:
#         title = title_list[0].text.strip()
#     else:
#         title = ''
#
#     content_list = soup.select('p')
#     if content_list:
#         content = content_list[0].text.strip()
#     else:
#         content = ''
#
#     figure_list = soup.select('figure', {'class': 'photo-layout'})
#     img_src = ''
#     if figure_list:
#         for figure in figure_list:
#             img_tag = figure.find('img')  # figure 태그 안에 있는 img 태그 찾기
#             if img_tag and 'src' in img_tag.attrs:
#                 img_src = img_tag['src']
#     else:
#         img_src = 'default'
#
#     # 제목, 내용 모두 있다면
#     if title != '' and content != '' and len(content) > 10:
#         # 테이블에 각각 아이디 넣어줘야함
#         # knowhow(title, content)
#         # knowhow category
#         # knowhow tag
#         # knowhow file
#         # knowhow plant
#         # print(title)
#         # print(content)
#         # print(img_src)
#
#         # 농어촌 - 농촌, 농업, 귀농, 농장, 농가, 농어촌, 농사
#         # 원예
#         # 꽃 - 생화, 조화, 꽃
#         # 조경
#         # 식물
#         if '원예' in content or '조경' in content:
#             category = '원예'
#             test_list.append([title, content, img_src, category])
#
#         elif '조화' in content or '생화' in content or '꽃' in content or '장미' in content or '국화' in content:
#             category = '꽃'
#             test_list.append([title, content, img_src, category])
#
#         elif '정원' in content or '가든' in content or '가드닝' in content:
#             category = '정원'
#             test_list.append([title, content, img_src, category])
#
#         elif '농촌' in content or '농업' in content or '귀농' in content or '농장' in content or '농가' in content or '농어촌' in content or '농사' in content:
#             category = '농촌'
#             test_list.append([title, content, img_src, category])
#
#
#
# print(test_list)
# # 데이터 프레임 csv로 내보내기
# # test_df = pd.DataFrame(test_list, columns=['Title', 'Content', 'Img_src', 'Category'])
# # test_df.to_csv('selleaf_test9.csv', index=False, encoding='utf-8-sig')
#
# print("CSV file has been created successfully.")