"""
[문제1] 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오.
<각 단계별 출력 결과 예시>
단계1:[10, 1, 5, 2, 10, 1, 5, 2]
단계2:[10, 1, 5, 2, 10, 1, 5, 2, 20]
단계3:[1, 2, 1, 2]

단계1: lst 원소를 2배 생성하여 result 변수에 저장 및 출력하기
단계2: lst의 첫 번째 원소에 2를 곱하여 result 변수에 추가 및 출력하기
단계3: result의 홀수 번째 원소만 result2 변수에 추가 및 출력하기
"""

lst = [10, 1, 5, 2]  # list 생성
print("단계1:", lst * 2)
# lst.append(lst[0] * 2)
lst = lst * 2
lst.append(lst[0] * 2)
print("단계2:", lst)
result = []
for i in range(len(lst)):
    if i % 2 != 0:
        result.append(lst[i])
print("단계3:", result)

"""
[문제2] list 원소 추가 및 요소 검사하기
A형 list 크기를 키보드로 입력 받은 후, 입력 받은 크기만큼 임의 숫자를 list에 추가하고, list의 크기를 출력하시오.
<출력 결과 예시>
vector 수 : 3
4
2
5
vector 크기 : 3
"""

import random

a = int(input('list의 크기:'))
b = []
for i in range(a):
    c = random.randint(1, 6)
    b.append(c)

print('vector 수:', a)
for i in b:
    print(i)
print('vector 크기:', a)
"""
B형 list크기를 키보드로 입력 받은 후, 입력 받은 크기만큼 임의 숫자를 list에 추가한다. 이후 list에서 찾을 값을
키보드로 입력한 후 해당 값이 list에 있으면 "YES", 없으면 "NO"를 출력하시오.
<출력 결과 예시>
vector 수 : 5
1
2
3
4
5
3
YES
"""

import random

a = int(input('list의 크기:'))
b = []
for i in range(a):
    c = random.randint(1, 6)
    b.append(c)

print('vector 수:', a)
for i in b:
    print(i)
    # if i == a:
    #     print("YES")
    # else:
    #     print("NO")
d = 0
for i in b:
    if i == a:
        d += 1

if d >= 1:
    print("YES")
else:
    print("NO")

"""
[문제3] list 내포를 이용하여 문자열 처리하기
A형 message 변수를 대상으로 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
<조건> list + for 형식 적용
<출력결과 예시>
[1, 0, 1, 0, 1]
"""
message = ['spam', 'ham', 'spam', 'ham', 'spam']
for i in range(len(message)):
    if message[i] == 'spam':
        message[i] = 1
    else:
        message[i] = 0
print(message)

"""
B형 message 변수를 대상으로 'spam' 원소만 추출하여 spam_list에 추가하시오.
<조건> list + for + if 형식 적용
<출력 결과 예시>
['spam', 'spam', 'sapm']
"""
message = ['spam', 'ham', 'spam', 'ham', 'spam']
spam_list = []
for i in message:
    if i == 'spam':
        spam_list.append(i)
print(spam_list)

"""
[문제4] position 변수를 대상으로 중복되지 않은 직위와 직위별 빈도수를 출력하시오.
<출력결과 예시>
중복되지 않은 직위 : ['사장', '과장', '대리', '부장']
각 직위별 빈도수 : {'과장':2, '부장':1, '대리':2, '사장':1}
"""
position = ['과장', '부장', '대리', '사장', '대리', '과장']
p = set(position)
p = list(p)
print("중복되지 않은 직위 :", p)
d = {}
for i in position:
    d[i] = d.get(i, 0) + 1
print("각 직위별 빈도수 :", d)
