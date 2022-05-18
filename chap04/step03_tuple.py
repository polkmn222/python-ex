# (1) 원소가 한 개인 경우
t = (10, )
print(t)

# (2) 원소가 여러 개인 경우
t2 = (1, 2, 3, 4, 5, 3)
print(t2)

# (3) 튜플 색인
print(t2[0], t2[1:4], t2[-1])

# (4) 수정 불가
# t2[0] = 10  # error

# (5) 요소 반복
for i in t2:
    print(i, end=' ')

# (6) 요소 검사
if 6 in t2:
    print("6 있음")
else:
    print("6 없음")

# (1) 튜플 자료형 반환
lst = list(range(1, 6))
t3 = tuple(lst)
print(t3)

# (2) 튜플 관련 함수
print(len(t3), type(t3))  # 5 <class 'tuple'>
print(t3.count(3))
print(t3.index(4))