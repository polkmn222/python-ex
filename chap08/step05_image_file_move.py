import os  # dir or file path
from glob import glob  # *, ? 파일 검색

# (1)  image 파일 경로
print(os.getcwd())  # C:\Users\user\Desktop\가마우지\python\myPackage
img_path = 'chapter08/images/'  # 이미지 원본 디렉터리
img_path2 = 'chapter08/images2/'  # 이미지 이동 디렉터리

# (2) 디렉터리 존재 유무
if os.path.exists(img_path):
    print('해당 디렉터리가 존재함')

    # (3) image 파일 저장, 파일 이동 디렉터리 생성
    images = []  # png 파일 저장
    os.mkdir(img_path2)  # 디렉터리 생성

    # (4) images 디렉터리에서 png 검색
    for pic_path in glob(img_path + '*.png'):  # png 검색
        # (5) 경로와 파일명 분리, 파일명 추가
        img_path = os.path.split(pic_path)
        images.append(img_path[1])  # png 파일명 추가

        # (6) 이진파일 읽기
        rfile = open(file=pic_path, mode='rb')
        output = rfile.read()

        # (7) 이진파일 쓰기 -> chapter08/png 폴더 이동
        wfile = open(img_path2 + img_path[1], mode='wb')
        wfile.write(output)

    rfile.close(); wfile.close()  # 파일 객체 닫기
else:
    print('해당 디렉터리가 없음')

print('png file=', images)