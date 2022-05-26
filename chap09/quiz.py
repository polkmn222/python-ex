"""
[문제1] login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.
<처리 조건>
1. <tr> 태그의 하위 태그인 <th> 태그의 모든 내용 출력
2. 각 단계 처리
<출력 결과>
th 태그 내용
아이디
비밀번호
"""
#<코딩 시작>
import random

from bs4 import BeautifulSoup
# 단계1. 파일 읽기
file = open('login.html', mode='r', encoding='utf-8')
source = file.read()

# 단계2. html 파싱
soup = BeautifulSoup(source, 'html.parser')
print(soup)

# 단계3. 태그 찾기
trs = soup.find_all('tr')
print(trs)

# 단계4. 태그 내용 출력
print('\nth tag 내용')
for i in trs:
    th = i.find('th')
    print(th.string)


"""
[문제2] login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.
<처리 조건>
1. id = "login_wrap" 선택자의 하위 태그 전체 출력
2. id = "login_wrap" 선택자 > form > table 태그 내용 출력
3. find_all('tr') 함수 이용 th 태그 내용 출력
"""
# <코딩 시작>
from bs4 import BeautifulSoup

# 1. html source 가져오기
file = open('login.html', mode='r', encoding='utf-8')
source = file.read()

# 2. html 파싱
soup = BeautifulSoup(source, 'html.parser')

# 3. 선택자 이용 태그 내용 가져오기
print('1. id 선택자')
div = soup.select_one("div#login_wrap")
print(div)
print()

print('2. id 선택자 > from > table')
table = soup.select_one("div#login_wrap > from > table")
print(table)
print()

print('3. table > tr > th/td 태그 내용 출력')
trs = soup.find_all("tr")
print(trs)
print('\nth 내용')
for i in trs:
    th = i.find('th')
    print(th.string)

print('\ntd input tag 내용')
for tr in trs:
    tds = tr.find('td')
    inp = tds.find('input')
    print(inp)

inputs = soup.find_all('input')
print(inputs)

print('\ninput 태그의 value 속성 값')
for inp in inputs:
    if 'value' in inp.attrs:
        value = inp.attrs['value']
        print(value)


"""
[문제3] iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.
<처리 조건>
1. iris.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
2. 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그리기
3. 1번 칼럼과 3번 칼럼을 대상으로 산점도 그래프 그린 후 5번 칼럼으로 색상 적용
"""
# <코딩 시작>
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('iris.csv')
print(iris.info())
# i1 = iris1['sepal.width']
# i3 = iris1['petal.width']
plt.scatter(iris['sepal.length'], iris['petal.length'])
# plt.show()
# i5 = iris1['variety']
# cdata = [random.randint(a=1, b=3) for i in range(10)]
# plt.scatter(x=i1, y=i3, c=cdata, marker='o')
plt.show()
# for i in iris1:
#     print(i)
print(iris['variety'].unique())
variety = []
for s in iris['variety']:
    if s == 'Setosa':
        variety.append(1)
    elif s == 'Versicolor':
        variety.append(2)
    else:
        variety.append(3)

plt.scatter(iris['sepal.length'], iris['petal.length'], c= variety)
plt.xlabel('sepal.length')
plt.ylabel('petal.length')
plt.title('sepal.length vs petal.length scatter plotting')
plt.show()
