# (1) dict 생성 방법1
dic = dict(key1 = 100, key2 = 200, key3 = 300)
print(dic)

# (2) dict 생성 방법2
person = {'name':'홍길동', 'age':35, 'address':'서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

# (3) 원소 수정, 삭제, 추가
# dict 원소 수정
person['age'] = 45
print(person)

# dict 원소 삭제
del person['address']
print(person) # {'name': '홍길동', 'age': 45}

# dict 원소 추가
person['pay'] = 350
print(person)  # {'name': '홍길동', 'age': 45, 'pay': 350}


# (1) 요소 검사
print(print(['age']))  # 45
print('age' in person)  # True

# (2) 요소 반복
for key in person.keys():  # key 넘김
    print(key)  # key 출력
for v in person.values(): # value 넘김
    print(v)  # value 출력

for i in person.items():  # (key, value) 넘김
    print(i)  #  ('name', '홍길동')


# (1) 단어 데이터 셋
charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {}  # 빈 셋

# (2) get() 함수 이용 : key 이용 value 가져오기
for key in charset:
    wc[key] = wc.get(key, 0) + 1  # get() 이용
print(wc)