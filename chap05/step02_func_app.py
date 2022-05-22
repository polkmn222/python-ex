import random
from statistics import mean, variance
from math import sqrt

dataset = [2, 4, 5, 6, 1, 8]


# (1) 산술 평균
def Avg(data):
    avg = mean(data)
    return avg


print('산술평균 =', Avg(dataset))


# (2) 분산/표준편차
def var_sd(data):
    avg = Avg(data)  # 함수 호출
    # list 내포
    diff = [(d - avg) ** 2 for d in data]

    var = sum(diff) / (len(data) - 1)
    sd = sqrt(var)

    return var, sd


# (3) 함수 호출
v, s = var_sd(dataset)
print('분산 =', v)
print('표준편차=', s)


# 피타고라스 정리
def pytha(s, t):
    a = s ** 2 - t ** 2
    b = 2 * s * t
    c = s ** 2 + t ** 2
    print("3변의 길이:", a, b, c)


pytha(2, 1)  # s, t의 인수는 양의 정수를 갖는다.


# 단계 1 : 동전 앞면과 뒷면의 난수 확률분포 함수 정의
def coin(n):
    result = []
    for i in range(n):
        r = random.randint(0, 1)
        if r == 1:
            result.append(1)  # 앞면
        else:
            result.append(0)  # 뒷면

    return result


print(coin(10))


# 단계 2 : 몬테카를로 시뮬레이션 함수 정의
def montaCoin(n):
    cnt = 0
    for i in range(n):
        cnt += coin(1)[0]  # coin 함수 호출
    result = cnt / n  # 누적 결과를 시행 횟수(n) 로 나눈다

    return result


# 단계 3 : 몬테카를로 시뮬레이션 함수 호출
print(montaCoin(10))
print(montaCoin(30))
print(montaCoin(100))
print(montaCoin(1000))
print(montaCoin(10000))


# (1) 튜플형 가변인수
def Func1(name, *names):
    print(name)  # 실인수 : 홍길동
    print(names)  # 실인수 : ('이순신', '유관순')


Func1("홍길동", "이순신", "유관순")

# statistics 모듈 import
from statistics import mean, variance, stdev


# (2) 통계량 구하는 함수
def statis(func, *data):
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        return 'TypeError'


# static 함수 호출
print('avg=', statis('avg', 1, 2, 3, 4, 5))
print('var=', statis('var', 1, 2, 3, 4, 5))
print('std=', statis('std', 1, 2, 3, 4, 5))


# (3) 딕트형 가변인수
def emp_func(name, age, **other):
    print(name)
    print(age)
    print(other)


# emp_func 함수 호출
emp_func('홍길동', 35, addr='서울시', height=175, weight=65)

