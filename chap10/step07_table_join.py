# use work;
# create or replace table emp(
#     eno int auto_increment primary key,
#     ename varchar(25) not null,
#     hiredate date not null,
#     pay int default 0,
#     bonus int default 0,
#     dname varchar(50)
# );
# alter table auto_increment = 1001;
# insert into emp(ename, hiredate, pay, bonus, dname) values('홍길동', '2008-03-10', 300, 15, '영업부');
# insert into emp(ename, hiredate, pay, bonus, dname) values('강호동', '2010-03-10', 250, 10, '판매부');
# insert into emp(ename, hiredate, pay, bonus, dname) values('유관순', '2008-03-10', 200, 10, '회계부');
# insert into emp(ename, hiredate, pay, bonus, dname) values('강감찬', '2007-01-10', 400, 25, '영업부');

# select * from emp;
# create or replace table dept(
#     dname varchar(50) not null,
#     daddr varchar(100)
# );

# insert into dept values('영업부', '뉴욕시');
# insert into dept values('판매부', '서울시');
# insert into dept values('회계부', '대전시');

# select * from dept;

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

    # (1) Table join
    pay = int(input('join 급여 입력 : '))
    sql = f"""
        select e.eno, e.ename, e.pay, d.dname, daddr
        from emp e inner join dept d
        on e.dname = d.dname and e.pay >= {pay}
    """

    # (2) 레코드 조회
    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3], row[4])

    print('검색된 레코드 수 :', len(data))

except Exception as e:
    print('db error :', e)
finally:
    cursor.close()
    conn.close()