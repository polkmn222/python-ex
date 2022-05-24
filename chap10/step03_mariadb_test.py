# show databases;  // 데이터 베이스 보기
# create database work;
# show databases;
# use work;  // db 선택
# create table goods(code int primary key, name varchar(20) not null, su int, dan int);
# show tables;
# insert into goods values(1,'냉장고',2,8500000);
# insert into goods values(2,'세탁기',3,5500000);
# insert into goods values(3,'전자레인지',2,350000);
# insert into goods values(4,'HDTV',3, 1500000);
# select * from goods;
# create user 'scott'@'localhost' identified by 'tiger';
# grant all privileges on work.* to 'scott'@'localhost';
# quit

# (1) 패키지 import
import pymysql

# (2) db연동 환경변수
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
    # (3) db 연동 객체
    conn = pymysql.connect(**config)
    # (4) sql문 실행 객체
    cursor = conn.cursor()

    # (5) 테이블 조회
    sql = "show tables"
    cursor.execute(sql)
    tables = cursor.fetchall()

    # (6) 전체 table 목록 출력
    print(tables)

    # (7) table 유무
    if tables:
        print('table 있음')
    else:
        print('talbe 없음')

except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()
    