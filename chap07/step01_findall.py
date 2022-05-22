import re  # 모듈 추가 - 방법 1
from re import findall  # 모듈 추가 - 방법 2

st1 = '1234 abc홍길동 ABC_555_6 이사도시'

# (1) 숫자 찾기
print(findall('1234', st1))
print(findall('[0-9]', st1))
print(findall('[0-9]{3}', st1))
print(findall('[0-9]{3,}', st1))
print(findall('\\d{3,}', st1))

# (2) 문자열 찾기
print(findall('[가-힣]{3,}', st1))
print(findall('[a-z]{3}', st1))
print(findall('[a-z|A-Z]{3}', st1))

# (3) 특정 위치의 문자열 찾기
st2 = 'test1abcABC 123mbc 45test'

# 접두어/접미어
print(findall('^test', st2))  # 접두어
print(findall('st$', st2))    # 접미어

# 종료 문자 찾기 : abc, mbc
print(findall('.bc', st2))

# 시작 문자 찾기
print(findall('t.', st2))

# (4) 단어 찾기(\\w) - 한글+영문+숫자
st3 = 'test^홍길동 abc 대한*민국 123$tbc'
words = findall('\\w{3,}', st3)

# (5) 문자열 제외 : x+(x가 1개 이상 반복)
print(findall('[^^*$]+', st3))  # 특수문제 제외
