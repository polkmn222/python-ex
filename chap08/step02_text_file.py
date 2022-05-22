# (1)  현재 작업디렉터리
import os
print('\n현재 경로 :', os.getcwd())  #  C:\Users\user\Desktop\가마우지\python\myPackage

# (2) 예외처리
try:
    # (3) 파일 읽기
    ftest1 = open('C:/Users/user/Desktop/python-ex/chap08/ftest.txt', mode='r')
    print(ftest1.read())  # 파일 전체 읽기

    # (4) 파일 쓰기
    ftest2 = open('C:/Users/user/Desktop/python-ex/chap08/ftest.txt', mode='w')
    ftest2.write('my first text~~~')  # 파일 쓰기

    # (5) 파일 쓰기 + 내용 추가
    ftest3 = open('C:/Users/user/Desktop/python-ex/chap08/ftest.txt', mode='a')
    ftest3.write('\nmy secent text ~~~') #  파일 쓰기(추가)
except Exception as e:
    print('Error 발생 : ', e)
finally:
    ftest1.close()
    ftest2.close()
    ftest3.close()


# 파일 읽기 관련 함수
try:
    # (1) read() : 전체 텍스트 자료 읽기
    ftest = open('C:/Users/user/Desktop/python-ex/chap08/ftest.txt', mode='r')
    full_text = ftest.read()
    print(full_text)
    print(type(full_text))

    # (2) readlinse() : 전체 텍스트 줄 단위 읽기
    ftest = open('C:/Users/user/Desktop/python-ex/chap08/ftest.txt', mode='r')
    lines = ftest.readline()  # list 반환
    print(lines)
    print(type(lines))  # <class 'list'>
    print('문단 수 :', len(lines))  # 문단 수 : 6

    # (3) list -> 문장 추출
    docs = []  # 문장 저장
    for line in lines:
        print(line.strip())
        docs.append(line.strip())

    print(docs)  # 문장 출력

    # (4) readline() : 한 줄 읽기
    ftest = open('C:/Users/user/Desktop/python-ex/chap08/ftest.txt', mode='r')
    line = ftest.readline()  # 한 줄 읽기
    print(line)
    print(type(line))  # <class 'list'>
except Exception as e:
    print('Error 발생 : ', e)
finally:
    ftest.close()  # 파일 객체 닫기

