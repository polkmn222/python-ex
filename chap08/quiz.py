"""
[문제1] ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어 수를 카운트 하시오.
<처리 조건>
1. 문장은 '\n'을 구분자로 한다.
2. 단어는 공백을 구분자로 한다.
<출력 결과>
문장 내용
[]
문장 수 : 6
단어 내용
[]
단어 수 : 22
"""
#<코딩 시작>
file = open('ftest.txt', mode='r')
lines = file.readlines()  # 줄 단위 전체 읽기
docs = []   # 문장 저장
words = []  # 단어 저장
# for i in lines:
#     a = str(i)
#     a = a.replace('\n', '')
#     docs.append(a)
# print('문장 내용')
# print(docs)
# print('문장 수 :', len(docs))
#
# for i in lines:
#     a = str(i)
#     a = a.replace('\n', '')
#     a = a.split(' ')
#     words.append(a)
# # print(words)
# ap = []
# for i in words:
#     ap = ap + i

# ap = set(ap)
# print('단어 내용')
# print(ap)
# print(ap.count(''))
# print(len(ap))
# lines = file.readlines()

# for i in docs:
#     b = str(i)
#     # print(b)
#     b = b.split(' ')
#     # b = b.split()
#     words.append(b)

# for i in range(len(docs)):
#     b = str(docs[i])
#     # print(b)
#     b = b.split(' ')
#     # b = b.split()
#     words.append(b)
# ap = []
# for i in range(len(words)):
#     ap.append(words[i])
# print('단어 내용')
# # print(words)
# print(len(ap))

for line in lines:
    docs.append(line.strip())
    for word in line.split():
        words.append(word)

print(docs)
print('문단 길이 :', len(docs))
print(words)
print('단어 길이 :', len(words))


"""
[문제2] emp.csv 파일을 읽어서 다음 출력 예시와 같이 출력하시오.
<출력 예시>
관측치 길이 : 5
전체 평균 급여 : 370.0
최저 급여 : 150, 이름 : 홍길동
최고 급여 : 500, 이름 : 강감찬
"""
# <코딩 시작>
import pandas as pd

# 1. file read
emp = pd.read_csv('emp.csv', encoding='utf-8')
print(emp.info())
print(emp)
print('관측치 길이 : ', len(emp))

pay = emp.pay
name = emp.name

print('전체 급여 평균 : ', pay.mean())
max_pay = max(pay)
min_pay = min(pay)

for i in range(len(pay)):
    if pay[i] == min_pay:
        print('최저 급여 : %d, 이름 : %s' % (min_pay, name[i]))
    if pay[i] == max_pay:
        print('최고 급여 : %d, 이름 : %s' % (max_pay, name[i]))