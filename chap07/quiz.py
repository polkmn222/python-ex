"""
[문제1] 다음과 같은 여러 줄의 문자열을 대상으로 <email 양식 처리조건>에 맞게 정규표현식을 적용하여 email양식이 올바른 것만 출력되도록 하시오.
<email 양식 처리조건>
1. 아이디 : 첫자는 영문소문자, 단어길이 4자 이상
2. 호스트 이름 : 영문소문자 시작, 단어길이 3자 이상
3. 최상위 도메인 : 영문소문자 3자리 이하
4. 정규표현식 기본 패턴 : '메타문자@메타문자.메타문자'
<출력 결과>
you2@naver.com
kimjs@gmail.com
"""

# <코딩 시작>

email = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""
from re import findall, match  # findall 함수 또는 match 함수 이용

for e in email.split(sep='\n'):
    p = findall('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]\\w{,2}', e)

    if p:
        a = p[0]
        print(a)
    p2 = match('^[a-z]\\w{3,}@[a-z]\\w{2,}.[a-z]\\w{,2}', e)

    if p2:
        print(e)

"""
[문제2] 다음 emp 변수는 '입사년도이름급여'순으로 사원의 정보가 기록된 자료이다. emp 변수를 이용하여 사원의 이름만 추출하는 함수를 정의하시오.
<출력 결과>
names = ['홍길동', '이순신', '유관순']
"""

# <코딩 시작>
from re import findall, sub

emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]


# 함수 정의
def name_pro(emp):

    names = []
    for e in emp:
        name = findall('[가-힣]{3}', e)
        names.append(name[0])
    return names


# 함수 호출
names = name_pro(emp)
print('names =', names)

"""
[문제3] 다음 emp 변수는 '입사년도이름급여'순으로 사원의 정보가 기록된 자료이다. emp 변수를 이용하여 사원의 이름만 추출하는 함수를 정의하시오.
<출력 결과>
전체 사원 급여 평균 : 260
"""
# <코딩 시작>
from re import findall
from statistics import mean

emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def pay_pro(emp):
    pays = []
    for e in emp:
        tmp = findall('[가-힣][0-9]{3}', e)
        pay = findall('[0-9]{3}', tmp[0])
        pays.append(int(pay[0]))
    return mean(pays)


# 함수 호출
pays_mean = pay_pro(emp)
print('전체 사원의 급여 평균 : ', pays_mean)

"""
[문제4] 다음 emp 변수는 '입사년도이름급여'순으로 사원의 정보가 기록된 자료이다. emp 변수를 이용하여 사원의 이름만 추출하는 함수를 정의하시오.
<출력 결과>
전체 급여 평균 : 260
평균 이상 급여 수령자
이순신 => 300
유관순 => 260
"""
# <코딩 시작>
from re import findall
from statistics import mean

emp = ["2014홍길동220", "2002이순신300", "2010유관순260"]

# 함수 정의
def pay_pro(x):
    from statistics import mean # 평균 함수
    import re
    tmp = [re.findall('[가-힣]{3}', user) for user in x]
    name = [user[0] for user in tmp]

    pay = []
    tmp = [re.findall('[가-힣][0-9]{3}', user) for user in x]
    for user in tmp:
        str_user = user[0]
        pay.append(int(str_user[1:]))
    pay_avg = mean(pay)
    print('전체 급여 평균 : %d' % pay_avg)
    print('평균 이상 급여 수령자')
    for i in range(len(x)):
        if pay[i] >= pay_avg:
            print(name[i], '=>', pay[i])


# 함수 호출
pay_pro(emp)


"""
[문제5] 다음 texts 변수의 텍스트를 출력 결과와 같이 전처리 하시오.
<출력 결과>
['afabasabag', 'abttaa', 'uysfsfaa']
"""
# <코딩 시작>
from re import findall, sub
texts = ['AFAB54747,asabag?', 'abTTa $$;a12:2424.', 'uysfsfA,A124&***$?']
texts1 = texts[0].lower()
texts1 = sub('[0-9]', '', texts1)
texts1 = sub('[,.?!;:$]', '', texts1)
print(texts1)
texts2 = texts[1].lower()
texts2 = sub('[0-9]', '', texts2)
texts2 = sub('[,.?!;:$]', '', texts2)
texts2 = sub('[ ]', '', texts2)
print(texts2)
texts3 = texts[2].lower()
texts3 = sub('[0-9]', '', texts3)
texts3 = sub('[,.?!;:$&*]', '', texts3)
print(texts3)