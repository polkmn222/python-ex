'''sqlite3 - 내장형 DBMS'''
# 패키지 import
import sqlite3
print(sqlite3.sqlite_version_info)  # (3, 37, 2)

try:
    # (1) db 연동 객체
    conn = sqlite3.connect("sqlite_db")  # db 생성 -> 연결 object
    # (2) sql 실행 객체
    cursor = conn.cursor()
    # (3) table 생성
    sql = 'create table if not exists test_table(name text(10), phone text(15), addr text(50))'
    cursor.execute(sql)  # sql문 실행
    # (4) 레코드 추가
    cursor.execute("insert into test_table values('홍길동','010-1111-1111','서울시')")
    cursor.execute("insert into test_table values('이순신','010-2222-2222','해남시')")
    cursor.execute("insert into test_table values('강감찬','010-3333-3333','평양시')") # db 반영

    # (5) 레코드 조회
    cursor.execute("select * from test_table")
    rows = cursor.fetchall()  # 조회 레코드 가져오기
    for row in rows:  # (6) 레코드 출력1
        print(row)

    print('이름 \t전화번호 \t 주소')  # (7) 레코드 출력2
    for row in rows:
        print(row[0],'\t',row[1],'\t',row[2])

except Exception as e:
    print('db 연동 실패 : ', e)
    conn.rollback()  # 실행 취소
finally:
    cursor.close()  # cursor 객체 닫기
    conn.close()

