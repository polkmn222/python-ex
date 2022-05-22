# (1-1) json 인코딩
import json

user = {'id': 1234, 'name': '홍길동'}  # Python Dict
print(type(user))  # <class 'dict'>
print(user['name'])  # 횽길동

# (1-2) json 인코딩
jsonString = json.dumps(user, ensure_ascii=False)  # ASCII 인코딩 적용 안함

# 문자열 출력
print(jsonString)  # {"id": 1234, "name": "홍길동"}
print(type(jsonString))  # <class 'str'>
# print(jsonString['name'])  # Error 발생

# (2) json 디코딩
pyObj = json.loads(jsonString)
print(type(pyObj))  # <class 'dict'>

# Dict 자료 확인
print(pyObj['name'])  # 홍길동
for key in pyObj:
    print(key, ':', pyObj[key])


# (1) json file 읽기
file = open('chapter08/data/usagov_bitly.txt', mode='r', encoding='utf-8')
lines = file.readlines()  # 줄 단위 전체 읽기

# (2) json 디코딩
# file(json 문자열) -> python dict 객체
rows = [json.loads(row) for row in lines]
print('rows :', len(rows))  # rows : 3560

# (3) 10개 원소 출력
for row in rows[:10]:
    print(row)  # 행 출력
    print(type(row))  # <class 'dict'>
file.close()

# (4) dict -> DataFrame 변환
import pandas as pd
recode_df = pd.DataFrame(rows)
print(recode_df.info())
