import json

# (1) json 파일 로드
file = open("labels.json", mode='r', encoding="utf-8")

# (2) decoding : json 문자열 -> dict
lines = json.load(file)
print(type(lines))  # <class 'list'>
print(len(lines))  # 30
print(type(lines[0]))  # <class 'dict'>

# (3) DataFrame 생성
import pandas as pd
df = pd.DataFrame(lines)
print(df.info())
print(df.head())

import pymysql

config = {
    'host': 'localhost',
    'user': 'scott',
    'password': 'tiger',
    'database': 'work',
    'port': 3307,
    'charset': 'utf8',
    'use_unicode': True
}

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # (4) Table 생성
    sql = """
    create table labels(
    id int not null,
    url varchar(150) not null,
    name varchar(50) not null,
    color varchar()50 not null,
    de char(5)
    )"""
    cursor.execute(sql)  # table 생성

    # (5) 레코드 조회
    cursor.execute("select * from labels")
    rows = cursor.fetchall()
    if rows:  # (6) 레코드 있는 경우
        print("labels 레코드 조회")
        for row in rows:
            print(row)
        print("전체 레코드 수 :", len(rows))
    else:  # (7) 레코드 없는 경우
        for i in range(30):
            uid = df.id[i]  # df.column
            url = df.url[i]
            name = df.name[i]
            color = df.color[i]
            de = str(df.default[i])  # boll -> str
            sql = f"insert into labels values({uid}, '{url}', '{name}', '{color}', '{de}')"
            cursor.execute(sql)
            conn.commit()  # db 반영
except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()
    