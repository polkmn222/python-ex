from bs4 import BeautifulSoup  # html 파싱

# (1) 로컬 파일 읽기
file = open("html02.html", mode='r', encoding='utf-8')
source = file.read()

# (2) html 파싱
html = BeautifulSoup(source, 'html.parser')

# (3) a 태그 찾기
links = html.find_all('a')  # list 반환
print('links size=', len(links))

# (4) a 태그에서 속성 찾기
for links in links:
    try:
        print(links.attr['href'])  # 5개
        print(links.attr['target'])  # error(1, 2, 3, 4, 5)
    except Exception as e:
        print('예외 발생 : ', e)


# (5) 정규표현식으로 속성 찾기
import re

print('패턴 객체 이용 속성 찾기')
patt = re.compile('http://')  # pattern object 생성
links = html.find_all(href=patt)  # 패턴 찾기
print(links)
