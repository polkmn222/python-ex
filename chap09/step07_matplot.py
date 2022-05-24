# (1) 패키지 import
import matplotlib.pyplot as plt  # 차트 생성
import random  # 차트 자료 생성
# 음수 부호 지원
import matplotlib
matplotlib.rcParams['axes.unicode_minus'] = False

# (2) 차트 자료 생성
print(random.randint(a=1, b=5))  # 1~5 난수 정수
print(random.random())  # 0~1 난수 실수
print(random.normalvariate(mu=0, sigma=1))
# 평균=0, 표준편차=1를 갖는 표준정규분포 난수


# (1) plot() 함수 도움말
help(plt.plot)
'''
plot(x, y)  # plot x and using default line style and color
plot(x, y, 'bo')  # plot y using blue circle markers
plot(y)  # plot y using x as index array 0..N-1
plot(y, 'r+')  # ditto, but with red plus ses
'''

# (2) 기본 차트 그리기

# (2-1) 1개 data
data = range(10)  # range(n) 동일 - 0~9
plt.plot(data)  # plot(y), x : index
plt.plot(data, 'r+')  # plot(y, 'r+')
plt.show()

# (2-2) 2개 data
data2 = [random.random() for i in range(10)]  # 난수 실수
plt.plot(data, data2)  # line

plt.plot(data, data2, 'ro')  # point
plt.show()


# (1) 산점도 그리기

# (1-1) 단색 산점도
plt.scatter(x=data, y=data2, c='b', marker='o')
plt.show()

# (1-2) 여러 가지 색 산점도
cdata = [random.randint(a=1, b=3) for i in range(10)]
print(cdata)
plt.scatter(x=data, y=data2, c=cdata, marker='o')
plt.show()

# (2) 히스토그램
data3 = [random.normalvariate(mu=0, sigma=1) for i in range(1000)]
plt.hist(data3)  # 정규분포
plt.show()

data4 = [random.uniform(a=1, b=100) for i in range(1000)]
plt.hist(data4)  # 균등분포
plt.show()