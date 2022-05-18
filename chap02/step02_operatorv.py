num1 = 100 # 피연산자1
num2 = 20  # 피연산자2

add = num1 + num2 # 덧셈
print('add=', add)
sub = num1 - num2 # 뺄셈
print('sub=', sub)
mul = num1 * num2 # 곱셈
print('mul=', mul)
div = num1 / num2 # 나눗셈
print('div=', div)
div2 = num1 % num2 # 나머지 계산
print('div2=', div2)
square = num1 ** 2 # 제곱 계산
print('square=', square)

# (1) 동등비교
bool_result = num1 == num2 # 두 변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2 # 두 변수의 값이 다른지 비교
print(bool_result)

# (2) 크기비교
bool_result = num1 > num2 # num1값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2 # num1값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2 # num2값이 큰지 비교
print(bool_result)
bool_result = num1 <= num2 # num2 값이 크거나 같은지 비교
print(bool_result)

# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <=10
print(log_result)

# 두 관계식 중 하나라도 같은지 판단
log_result = num1 >= 50 or num2 <=10
print(log_result)

log_result = num1 >= 50 # 관계식 판단
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50) 
print(log_result)

# (1) 변수에 값 할당(=)
i = tot = 10 # i=10; tot = 10
i += 1 # i = i + 1
tot += i # tot = tot + i
print(i, tot)

# 같은 줄에 중복 출력
print('출력1', end='  ,  ') # end='구분자'

v1, v2 = 100, 200

# (2) 변수 교체
v2, v1 = v1, v2
print(v1, v2) # 200 100

# (3) 패킹(paking) 할당
lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
print(v1, v2) # 1 [2, 3, 4, 5]

*v1, v2 = lst
print(v1, v2) # [1, 2, 3, 4] 5

