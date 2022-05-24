''' CRUD : Create, Read, Update, Delete '''
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

    # (1) table 생성
    sql = """create table goods(code int primary key, name varchar(20) not null, su int default 0, dan int default 0)"""
    cursor.execute(sql)

    # (2) 레코드 추가
    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su = int(input('su 입력 : '))
    dan = int(input('dan 입력 : '))

    sql = "insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()  # db 반영

    # (3) 전체 목록 보기
    sql = "select * from goods"
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()  # 전체 검색

    # 레코드 출력 : 양식문자
    for r in rows:  # fetchone()
        # print(r)  # tuple type 출력
        print('%d   %s  %d  %d' % r)
    print('검색 레코드 수 :', len(rows))

    # (4) 상품명 조회
    name = input('\n조회할 상품명 입력 : ')
    sql = f"select * from goods where name like '%{name}'"
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()

    if rows:
        # 레코드 1개 출력 : index 이용
        for r in rows:
            print(r[0], r[1], r[2], r[3])
    else:
        print('해당 상품 없음')
except Exception as e:
    print('db 연동 오류 : ', e)
    # (5) 이전 상태 리턴
    conn.rollback()
finally:
    cursor.close()
    conn.close()




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

    # (1) table 생성
    sql = """create table goods(code int primary key, name varchar(20) not null, su int default 0, dan int default 0)"""
    cursor.execute(sql)

    # (2) 레코드 추가
    code = int(input('code 입력 : '))
    name = input('name 입력 : ')
    su = int(input('su 입력 : '))
    dan = int(input('dan 입력 : '))

    sql = "insert into goods values({code}, '{name}', {su}, {dan})"
    cursor.execute(sql)
    conn.commit()  # db 반영

    # (5) 레코드 수정
    # code -> 상품명, 수량, 단가 수정
    '''
    code = int(input('수정 code 입력 : '))
    name = input('수정 name 입력 : ')  
    su = int(input('수정 su 입력 : '))
    sql = f"update goods set name = '{name}',su = {su}, dan = {dan}, where code = {code}"
    cursor.execute(sql)
    conn.commit() 
    '''
    # (6) 레코드 삭제
    code = int(input('삭제 code 입력 : '))
    sql = f"delete from goods where code = {code}"
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()

    if rows:
        # 레코드 1개 출력 : index 이용
        print('레코드 삭제')
        '''
        sql = f"delete from goods where code = {code}"
        cursor.execute(sql)  # sql문 실행
        conn.commit()
        '''
    else:
        print('해당 code 없음')


    # (3) 전체 목록 보기
    sql = "select * from goods"
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()  # 전체 검색

    # 레코드 출력 : 양식문자
    for r in rows:  # fetchone()
        # print(r)  # tuple type 출력
        print('%d   %s  %d  %d' % r)
    print('검색 레코드 수 :', len(rows))

    # (4) 상품명 조회
    name = input('\n조회할 상품명 입력 : ')
    sql = f"select * from goods where name like '%{name}'"
    cursor.execute(sql)  # sql문 실행
    rows = cursor.fetchall()

    if rows:
        # 레코드 1개 출력 : index 이용
        for r in rows:
            print(r[0], r[1], r[2], r[3])
    else:
        print('해당 상품 없음')
except Exception as e:
    print('db 연동 오류 : ', e)
    # (5) 이전 상태 리턴
    conn.rollback()
finally:
    cursor.close()
    conn.close()
