# re 모듈관련 함수 import
from re import findall, sub

# 텍스트 전처리
texts = ['우리나라    대한민국, 우리나라%$ 만세', '비아그&라 500GRAM 정력 최고!', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']


# (1) 텍스트 전처리 함수
def crean_text(text): # 문장 인수
    # 1~6 단계
    texts_re = text.lower()  # 소문자 변경
    texts_re2 = sub('[0-9]', '', texts_re)  # 숫자 제거
    texts_re3 = sub('[,.?;:]', '', texts_re2)  # 문장부호 제거
    texts_re4 = sub('[@#$%^&*()]', '', texts_re3)  # 특수문자 제거
    texts_re5 = sub('[a-z]', '', texts_re4)  # 영문자 제거
    texts_re6 = ' '.join(texts_re5.split())  # white space 제거
    return texts_re6


# (2) 함수 호출
texts_result = [crean_text(text) for text in texts]
print(texts_result)
# 출력 결과
'''
['우리나라 대한민국 우리나라 만세', '비아그라 정력 최고!', '나는 대한민국 사람', '보험료 원에 평생 보장 마감 임박', '나는 홍길동']
'''