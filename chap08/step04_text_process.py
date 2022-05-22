import os  # os 모듈 import

# (1) 텍스트 디렉터리 경로 지정
print(os.getcwd())  # 기본 작업 디렉터리
txt_data = 'chapter08/txt_data/'  # 상대경로 지정

# (2) 텍스트 디렉터리 목록 반환
sub_dir = os.listdir(txt_data)  # txt_data 목록 반환
print(sub_dir)


# (3) 각 디렉터리의 텍스트 자료 수집 함수
def textPro(sub_dir):  # ['first', 'second']
    first_txt = []  # first 디렉터리 텍스트 저장
    second_txt = []  # second 디렉터리 텍스트 저장

    # (3-1) 디렉터리 구성
    for sdir in sub_dir:  # ['first', 'second']
        dirname = second_txt + sdir  # 디렉터리 구성
        file_list = os.listdir(dirname)  # 파일 목록 반환

        # (3-2) 파일 구성
        for fname in file_list:
            file_path = dirname + '/' + fname  # 파일 구성

            # (3-3) file 선택
            if os.path.isfile(file_path):
                try:
                    # (3-4) 텍스트 자료 수집
                    file = open(file_path, 'r')
                    if sdir == 'first':
                        first_txt.append(file.read())
                    else:
                        second_txt.append(file.read())
                except Exception as e:
                    print('예외 발생 :', e)
                finally:
                    file.close()

    return first_txt, second_txt  # 텍스트 자료 반환


# (4) 함수 호출
first_txt, second_txt = textPro(sub_dir)  # ['first', 'second']

# (5) 수집한 텍스트 자료 확인
print('first_tex 길이 = ', len(first_txt))
print('second_tex 길이 =', len(second_txt))

# (6) 텍스트 자료 결합
tot_texts = first_txt + second_txt
print('tot_texts 길이=', len(tot_texts))

# (7) 전체 택스트 내용
print(tot_texts)
print(type(tot_texts))

# (1) pickle 모듈 import
import pickle  # file save

# (2) file save : write binary
pfile_w = open("chapter08/tot_texts.pck", mode='wb')
pickle.dump(tot_texts, pfile_w)

# (3) file load : read binary
pfile_r = open("chapter08/tot_texts.pck", mode='rb')
tot_texts_read = pickle.load(pfile_r)
print('tot_texts 길이 = ', len(tot_texts_read))
print(type(tot_texts_read))
print(tot_texts_read)
