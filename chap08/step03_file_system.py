import os  # os 모듈 import

# 현재 작업 디렉터리 경로 확인
print(os.getcwd())  # C:\Users\user\Desktop\가마우지\python\myPackage

# 작업 디렉터리 변경 : 'chapter08' 이동
os.chdir('chapter08')
print(os.getcwd())  # C:\Users\user\Desktop\가마우지\python\myPackage\chapter08

# 현재 작업 디렉터리 목록 : list 반환
print(os.listdir('.'))

# 디렉터리 생성 : 'test' 생성
os.mkdir('test')
print(os.listdir('.'))

# 디렉터리 이동 : 'test' 이동
os.chdir('test')
print(os.getcwd())  # C:\Users\user\Desktop\가마우지\python\myPackage\chapter08\test

# 여러 디렉터리 생성 : 'text2', 'text3' 생성
os.makedirs('test2/test3')
print(os.listdir('.'))

# 디렉터리 이동 : 'test' 이동
os.chdir('test2')
print(os.listdir('.'))

# 디렉터리 삭제 : 'test3' 삭제
os.rmdir('test3')
print(os.listdir('.'))  # []

# 상위 디렉터리 이동 : 상위 디렉터리 2개 이동
os.chdir('../..')
print(os.getcwd())

# 여러 개의 디렉터리 삭제 : 'test', 'test2' 삭제
os.removedirs('test/test2')

import os.path  # window 파일 경로를 조작하는 모듈

# 현재 경로 확인
print(os.getcwd())  # C:\Users\user\Desktop\가마우지\python\myPackage

# 경로 변경
os.chdir('chapter08')  # C:\Users\user\Desktop\가마우지\python\myPackage\chapter08
print(os.getcwd())

# lecture 디렉터리의 step01_try_except.py 파일 절대경로
print(os.path.abspath(
    'step01_try_except.py'))  # C:\Users\user\Desktop\가마우지\python\myPackage\chapter08\step01_try_except.py

# step01_try_except.py 파일의 디렉터리 이름
print(os.path.dirname('chapter08/step01_try_except.py'))  # chapter08

# worksapce 디렉터리 유무 확인
print(os.path.exists('C:/Users/user/Desktop/가마우지/python/myPackage'))  # True

# step01_try_except.py 파일 유무 확인
print(os.path.isfile('step01_try_except.py'))  # True

# chapter08 디렉터리 유무 확인
print(os.path.isdir('chapter08'))  # True

# 디렉터리와 파일 분리
print(os.path.split("C:\\test\\test1.txt"))  # ('C:\\test', 'test1.txt')
# 디렉터리와 파일 결합
print(os.path.join('C:\\test', 'test1.txt'))  # C:\test\test1.txt

# step01_try_except.py 파일 크기
print(os.path.getsize('step01_try_except.py'))  # 1188