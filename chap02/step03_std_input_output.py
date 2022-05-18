"""
# (1) 문자형 숫자 입력
num = input("숫자 입력 : ")
print('num type : ', type(num) ) # <class 'str'>
print('num = ', num)
print('num = ', num * 2)

# (2) 문자형 숫자를 정수형으로 변환
num1 = int (input("숫자 입력 : ") ) # str -> int(형변환)
print('num1 = ', num1 * 2)

# (3) 문자형 숫자를 실수형으로 변환
num2 = float(input("숫자 입력 : ")) # str -> float(형변환)
result = num1 + num2 # 실수 = 정수 + 실수
print('result = ', result)
"""

# (1) value 인수
print("value = ", 10 + 20 + 30 + 40 + 50)

# (2) sep 인수 : 값과 값을 특수문자로 구분
print("010", "1234", "5678", sep="-")

# (3) end 인수
print("value=", 10, end = ", ")
print("value=", 20)

# (4) format() 함수 인수 : format(value, "format")
print("원주율=", format(3.14159, "8.3f"))
print("금액 = ", format(10000, "10d"))
print("금액 = ", format(125000, "3,d"))

# (5) 양식문자 인수 : print( "%양식문자" %(값))
name = "홍길동"
age = 35
price = 125.456
print("이름 : %s, 나이 : %d, data = %.2f" %(name, age, price) )

# (6) 외부 상수 인수
print("이름 : {}, 나이 : {}, data={}".format(name, age, price) )
print("이름 : {1}, 나이 : {0}, data={2}".format(age, name, price) )

# (7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"select * from member uid = {uid}"
print(query) # member 테이블에서 uid가 hong인 레코드 검색
