"""
[문제1] 다음 height 변수에 별(star)의 층수를 입력하면 각 층마다 별의 개수가 한 개씩 증가하여 출력되고,
마지막 줄에 멸의 개수가 출력되도록 함수의 빈칸을 채우시오.
"""
# # 함수 정의
# def StarCount(height):
#     count = 0
#     for i in range(1, height + 1):
#         print("*" * i)
#         count += i
#     return count
#
# # 키보드 입력
# height = int(input('height : '))
# # start 개수 줄력
# print('start 개수 :  %d' % StarCount(height))

"""
[문제2] 중첩함수를 적용하여 다음<조건>에 맞게 은행계좌 함수의 빈 칸을 채우시오.
<조건1> 외부함수 : bank_account() : 잔액(balance) outer 변수
<조건2> 내부함수 : getBalance() : 잔액 확인
                 deposit(money) : 입금하기
                 withdraw(money) : 출금하기
<조건3> 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.' 메시지 출력
<조건4> 기타 나머지는 출력 예시 참조 

<출력 결과 예시>
최초 계좌의 잔액을 입력하세요 : 1000
현재 계좌 잔액은 1000원 입니다.
입금액을 입력하세요 : 15000
15000원 입금후 잔액은 16000원 입니다.
출금액을 입력하세요 : 3000
3000원 출금후 잔액은 13000원 입니다.                
"""
# 함수 정의
def bank_account(bal):
    balance = bal  # 잔액 초기화(1000)

    def getBalance():  # 잔액 확인(getter)
        return balance

    def deposit(money):  # 입금하기(setter)
        nonlocal balance
        balance += money

    def withdraw(money):  # 출금하기(setter)
        nonlocal balance
        if balance < money:
            print("잔액이 부족합니다")
        else:
            balance -= money

    return getBalance(), deposit(), withdraw()  # 클로저 함수 리턴


"""
[문제3] 팩토리얼(Factorial)을 계산하는 재귀함수의 빈 칸을 채우시오.
예) 5!(5*4*3*2*1) = 120
"""
# 재귀 함수 정의
def Factorial(n):
    if n == 1:  # 종료 조건
        return 1
    else:
        result = n * Factorial(n-1)
        return result


# 함수 호출
result_fact = Factorial(5)
print('팩토리얼 결과: ', result_fact)