# (1) 예외 발생 코드
print('프로그램 시작 !!!')
x = [10, 30, 25.2, 'num', 14, 51]

# for i in x:
#     print(i)
#     y = i ** 2  # 예외 발생
#     print('y =', y)
#
# print('프로그램 종료')

# (2) 예외 처리 코드
print('프로그램 시작 !!!')
for i in x:
    try:
        y = i ** 2  # 예외 발생
        print('i=', i, ',y =', y)
    except:  # except 블록
        print('숫자 아님 : ', i)

print('프로그램 종료')


# 유형별 예외처리
print('\n유형별 예외처리')
try:
    div = 1000 / 2.53
    print('div = %5.2f' % div)  # 정상
    div = 1000 / 0            # 1차: 산술적 예외
    f = open('C:\\test.txt')  # 2차: 파일열기
    num = int(input('숫자 입력 : '))  # 3차: 기타 예외
    print('num =', num)
# 다중 예외처리 클래스
except ZeroDivisionError as e:  # 산술적 예외처리
    print('오류정보 : ', e)
except FileNotFoundError as e:  # 파일 열기 예외처리
    print('오류정보 : ', e)
except Exception as e:  # 기타 예외 처리
    print('오류정보 : ', e)
finally:
    print('finally 영역 - 항상 실행되는 영역')
    