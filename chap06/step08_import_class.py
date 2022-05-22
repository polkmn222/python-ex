# (1)  리스트 열거형 객체 이용
lst = [1, 3, 5]
for i, c in enumerate(lst):
    print('색인 : ', i, end=', ')
    print('내용 :', c)

# (2) 튜플 열거형 객체 이용
dit = {'name' : '홍길동', 'job' : '회사원', 'addr' : '서울시'}
for i, k in enumerate(dit):
    print('순서 : ', i, end=', ')
    print('키 : ', k, end=', ')
    print('값 : ', dit[k])


# (1) 모듈 내장클래스 import
import datetime  # 모듈 import
from datetime import date, time

# (2) date 클래스
help(date)  # date 클래스 도움말

today = date(2022, 5, 20)  # date 객체 생성
print(today)  # date 객체 정보

# date 객체 멤버변수 호출
print(today.year)  # 2022
print(today.month) # 5
print(today.day)   # 20

# date 객체 메서드 호출
w = today.weekday()  # Monday == 0 ... Sunday == 6
print('요일 정보 : ', w)  # 요일정보

# (3) time 클래스
help(time)  # time 클래스 도움말

currTime = time(21, 4, 30)  # time 객체 생성
print(currTime)  # time 객체 정보

# time 객체 멤버변수 호출
print(currTime.hour)   # 21
print(currTime.minute) #  4
print(currTime.second) # 30

# time 객체 메서드 호출
isoTime = currTime.isoformat()  # HH:MM:SS
print(isoTime)
