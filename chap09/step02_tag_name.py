import urllib.request
import fimport
from bs4 import BeautifulSoup  # html 파싱

# (1) 로컬 서버 파일 읽기
file = open('html01.html', mode='r', encoding='utf-8')
text = file.read()

# (2) html 파싱
html = BeautifulSoup(text, 'html.parser')

# (3) 태그 내용 가져오기

# (3-1) tag 이용
h1 = html.html.body.h1  # 계층 접근
print('h1 :', h1.string)  #  h1 : 시멘틱 태그 ?

# (3-2) find('tag') 함수
h2 = html.find('h2')
print('h2 :', h2.string)  # h2 :  주요 시멘틱 태그

# (3-3) find_all('tag') 함수
lis = html.find_all('li')  # list 반환
print(lis)

# (4) li 태그 내용
for li in lis:
    print(li.string)

