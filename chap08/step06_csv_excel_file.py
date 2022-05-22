# (1) pandas 패키지 import
import pandas as pd
import os
# 현재 작업 디렉터리 확인
print(os.getcwd())  #  C:\Users\user\Desktop\가마우지\python\myPackage\chapter08

# (2) csv 파일 읽기
score = pd.read_csv('chapter08/data/score.csv')
print(score.info())  # 파일 정보
print(score.head())  # 칼럼명 포함 앞부분 5개 행

# (3) 칼럼 추출
kor = score.kor  # 객체['칼럼명']
eng = score['eng']  # 객체['칼럼명']
mat = score['mat']  # 객체['칼럼명']
dept = score['dept']  # 객체['칼럼명']

# (4) 과목별 최고 점수
print('max kor = ', max(kor))
print('max eng = ', max(eng))
print('max mat = ', max(mat))

# (5) 과목별 최하 점수
print('min kor = ', min(kor))
print('min eng = ', min(eng))
print('min mat = ', min(mat))

# (6) 과목별 평균 점수
from statistics import mean
print('국어 점수 평균 : ', round(mean(kor), 3))
print('영어 점수 평균 : ', round(mean(eng), 3))
print('수학 점수 평균 : ', round(mean(mat), 3))

# (7) dept 빈도수
dept_count = {}  # 빈 set

for key in dept:
    dept_count[key] = dept_count.get(key, 0) + 1

print(dept_count)  # dict


# (1) excel 파일 읽기
sam = pd.ExcelFile('chapter08/data/sam_kospi.xlsx')

# (2) excel 파싱
kospi = sam.parse("sam_kospi")
print(kospi.info())

# (3) 칼럼 추출
high = kospi['High']
low = kospi['Low']

# (4) 평균 계산
from statistics import mean
print('high mean=', mean(high))
print('low mean=', mean(low))

# (5) 평균 계산
print('High mean : ', high.mean())
print('Low mean : ', low.mean())