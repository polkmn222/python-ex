# (1) builtins 함수
help(len)
dataset = list(range(1, 6))
print(dataset)

print('len=', len(dataset))
print('sum=', sum(dataset))  # sum = 15
print('max=', max(dataset))
print('min=', min(dataset))

# (2) import 함수
import statistics  # (방법1)
from statistics import variance, stdev  # (방법2)

print('평균=', statistics.mean(dataset))  # (방법1)
print('중위수=', statistics.median(dataset))  # (방법1)
print("표준 분산=", variance(dataset))  # (방법2)
print("표준 표준편차=", stdev(dataset))  # (방법2)


# (1) 인수가 없는 함수
def userFunc1():
    print('인수가 없는 함수')
    print('userFunc1')


userFunc1()


# (2) 인수가 있는 함수
def userFunc2(x, y):
    print('userFunc2')
    z = x + y
    print('z=', z)


userFunc2(10, 20)  # 함수 호출


# (3) return 있는 함수
def userFunc3(x, y):
    print('userFunc3')
    tot = x + y
    sub = x - y
    mul = x * y
    div = x / y

    return tot, sub, mul, div

# 실인수 : 키보드 입력
x = int(input('x 입력 : '))
y = int(input('y 입력 : '))

t, s, m, d = userFunc3(x, y)
print('tot=', t)
print('sub=', s)
print('mul=', m)
print('div=', d)