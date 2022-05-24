# 모듈 import
import urllib.request as req
from bs4 import BeautifulSoup

# news 제공 포털 사이트
url = "http://media.daum.net"

# (1) url 요청
res = req.urlopen(url)
source = res.read()

# (2) source 디코딩
source = source.decode("utf-8")  # charset="utf-8"

# (3) html 파싱
html = BeautifulSoup(source, 'html.parser')

# (4) tab[속성=값] 요소 추출
atags = html.select('a[class=link_txt]')
print('a tag 수 =', len(atags))  # a tag 수 = 32

# (5) a 태그 내용 수집
crawling_data = []  # 빈 list

cnt = 0
for atag in atags:
    cnt += 1
    atagStr = str(atag.string)  # string 변환
    crawling_data.append(atagStr.strip())
    '''
    string.strip() : 문단 끝 불용어(공백, tab, \n\r) 제거
    '''
# 수집한 자료 확인
print('수집한 자료 확인')
print(crawling_data)

# (6) pickle save/load
import pickle  # object -> file(binary) -> load(object)
# save : binary file save
file = open('data.pickle', mode='wb')
pickle.dump(crawling_data, file)

# load : binary file load
file = open('data.pickle', mode='rb')
crawling_data = pickle.load(file)
print('pickle load')
print(crawling_data)
