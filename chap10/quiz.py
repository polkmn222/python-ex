"""
[문제1] 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.
<처리 조건>
1. [레코드 처리 메뉴]에서 메뉴 번호를 키보드로 입력받아서 레코드를 관리한다.
2. [레코드 처리 메뉴]는 다음과 같다.

[레코드 처리 메뉴]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력:
<각 메뉴 작업 절차>
1번 입력 : 전체 레코드 조회 결과 출력
2번 입력 : 키보드 입력(상품코드, 상품명, 수량, 단가) -> 레코드 추가
3번 입력 : 키보드 입력(상품코드, 수량, 단가) -> 레코드 수정(수량, 단가 수정)
4번 입력 : 키보드 입력(상품코드) -> 레코드 삭제
5번 입력 : 프로그램 종료
"""
# <코딩 시작>
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

    while True:  # 무한 루프
        print('\t[레코드 처리 메뉴]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')
        menu = int(input('\t메뉴번호 입력 : '))

        if menu == 1:
            # 1. 레코드 조회
            sel = int(input('1.전체 조회, 2. 상품명 조회 :'))
            if sel == 1:
                sql = "select * from goods"
                cursor.execute(sql)
                dataset = cursor.fetchall()

                for row in dataset:
                    print(row[0], row[1], row[2], row[3])
                print('검색된 레코드 수 : ', len(dataset))
            elif sel == 2:
                name = input('상품명 입력 : ')
                sql = f"select * from goods where name like '%{name}%'"
                cursor.execute(sql)
                dataset = cursor.fetchall()

                if dataset:
                    for row in dataset:
                        print(row)
                else:
                    print('검색된 레코드 없음')
        elif menu == 2:
            # 2. 레코드 추가
            code = int(input('code 입력 : '))
            name = input('name 입력 : ')
            su = int(input('su 입력 : '))
            dan = int(input('dan 입력 : '))

            sql = "insert into goods values({code}, '{name}', {su}, {dan})"
            cursor.execute(sql)
            conn.commit()  # db 반영
        elif menu == 3:
            # 3. 레코드 수정
            code = int(input('수정 code 입력 : '))
            name = input('수정 name 입력 : ')
            su = int(input('수정 su 입력 : '))
            sql = f"update goods set name = '{name}',su = {su}, dan = {dan}, where code = {code}"
            cursor.execute(sql)
            conn.commit()
        elif menu == 4:
            # 4. 레코드 삭제
            code = int(input('삭제 code 입력 : '))
            sql = f"delete from goods where code = {code}"
            cursor.execute(sql)  # sql문 실행
            conn.commit()
        elif menu == 5:
            print('프로그램 종료')
            break
        else:
            print('해당 메뉴는 없습니다.')

# DB 연결 예외 처리
except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()


"""
[문제2] bmi_tab 테이블 대상으로 다음과 같은 조건으로 테이블을 검색하시오.
<처리 조건>
1. 키(height)가 170~180 사이에 해당하는 레코드 조회
2. 키보드로 'thin', 'normal', 'fat' 중 하나를 입력하여 label에 속하는 레코드 출력하기(like 명령어 사용)
"""
# <코딩 시작>
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
    # <조건1> 키 170~180 사이 검색
    sql = "select * from bmi_tab where height >= 170 and height <= 180"
    cursor.execute(sql)

    rows = cursor.fetchall()
    for row in rows:
        print(row[0], row[1], row[2])

    print('전체 레크도 수 :', len(rows))

    # <조건2> label 조회
    label = input('검색할 label 입력 : ')
    sql = f"select * from bmi_tab where label like '%{label}%'"
    cursor.execute(sql)
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
        print('해당 label의 레코드 수 : ', len(rows))
    else:
        print('해당 label 없음')

# DB 연결 예외 처리
except Exception as e:
    print('db 연동 오류 :', e)
    conn.rollback()
finally:
    cursor.close()
    conn.close()