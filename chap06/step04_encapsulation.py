class Account:
    # (1) 은닉 멤버변수
    __balance = 0 # 잔액
    __accName = None # 예금주
    __accNo = None # 계좌번호

    # (2) 생성자 : 멤버변수 초기화
    def __init__(self, bal, name, no):
        self.__balance = bal  # 잔액 초기화
        self.__accName = name # 예금주
        self.__accNo = no     # 계좌번호

    # (3) 계좌정보 확인 : Getter
    def getBalance(self):
        return self.__balance, self.__accName, self.__accNo

    # (4) 입금하기 : Setter
    def deposit(self, money):
        if money < 0:
            print('금액 확인')
            return  # 종료(exit)
        self.__balance += money

    # (5) 출금하기 : Setter
    def withdraw(self, money):
        if self.balance < money:
            print('잔액부족')
            return  # 종료(exit)
        self.__balance -= money

# (6) object 생성
acc = Account(1000, '홍길동', '125-152-4125-41')  # 생성자

# (7) Getter 호출
# acc.__balance # 오류(Error)
bal = acc.getBalance()
print('계좌정보 : ', bal)

# (8) Setter 호출
acc.deposit(10000)  # 10000원 입금
bal = acc.getBalance()
print('계좌정보 : ', bal)  # 입금 확인