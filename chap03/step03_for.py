# (1) 문자열 열거형객체 이용
import random

string = "홍길동"
print((len(string))) # 문자 길이 : 3
for s in string: # 1문자 -> 변수 넘김 : 3회
    print(s)

# (2) list 열거형객체 이용
lstset = [1, 2, 3, 4, 5] # 5개 원소를 갖는 열거형 객체

for e in lstset:
    print('원소 : ', e)

# (1) range 객체 생성
num1 = range(10) # range(start)
print('num1 : ', num1)
num2 = range(1, 10) # range(start, stop)
print('num2 : ', num2)
num3 = range(1, 10, 2) # range(start, stop, step)
print('num3 : ', num3)

# (2) range 객체 활용
for n in num1:
    print(n, end=' ')
print()
for n in num2:
    print(n, end=' ')
print()
for n in num3:
    print(n, end=' ')

# (1) list에 자료 저장하기
lst = [] # 빈 list 만들기
for i in range(10): # 0 ~ 9
    r = random.randint(1, 10) # 난수 발생
    lst.append(r) # 난수 저장

print('lst=', lst) # 난수 출력

# (2) list에 자료 참조하기
for i in range(10): # 0 ~ 9
    print(lst[i] * 0.25) # 난수 * 0.25


# 구구단 출력 : range() 함수 이용

# (1) 바깥쪽 반복문
for i in range(2, 10):
    print('~~~ {}단 ~~~'.format(i))

    # (2) 안쪽 반복문
    for j in range(1, 10):
        print('%d * %d = %d' % (i, j, i * j))

string = """나는 홍길동 입니다.
주소는 서울시 입니다.
나이는 35세 입니다."""

sents = [] # 문장 저장
words = [] # 단어 저장

# (1) 문단 -> 문장
for sen in string.split(sep= "\n"):
    sents.append(sen)
    # (2) 문장 -> 단어
    for word in sen.split():
        words.append(word)

print('문장 : ', sents)
print('문장수 : ', len(sents))
print('단어 : ', words)
print('단어수 : ', len(words))
