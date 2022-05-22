# (1) 일반 함수
def Adder(x, y):
    add = x + y
    return add


print('add=', Adder(10, 20))

# (2) 람다 함수
print('add=', (lambda x, y: x + y)(10, 20))

# (1) 지역변수 예
x = 50  # 전역변수


def local_func(x):
    x += 50  # 지역변수 -> 종료 시점 소멸


local_func(x)
print('x=', x)


# (2) 전역변수 예
def global_func():
    global x  # 전역변수 x 사용
    x += 50  # x + 50 = 100


global_func()
print('x=', x)

