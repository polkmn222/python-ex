# (1) 생성자 이용 멤버변수 초기화
class multiply:
    # 멤버변수
    x = y = 0

    # 생성자 : 초기화
    def __init__(self, x, y):  # 객체만 생성
        self.x = x
        self.y = y

    # 메서드
    def mul(self):
        return self.x * self.y


obj = multiply(10, 20)  # 생성자
print('곱셈 = ', obj.mul())


# (2) 메서드 이용 멤버변수 초기화
class multiply2:
    # 멤버변수
    x = y = 0

    # 생성자 없음 : 기본 생성자 제공
    def __init__(self):
        pass

    # 메서드 : 멤버변수 초기화
    def data(self, x, y):
        self.x = x
        self.y = y

    # 메서드 : 곱셈
    def mul(self):
        return self.x * self.y


obj = multiply2()  # 기본 생성자
obj.data(10, 20)  # 동적 멤버 변수 생성
print('곱셈 = ', obj.mul())


class multiply3:
    # 멤버변수 없음
    # 생성자 없음

    # 동적 멤버변수 생성/초기화
    def data(self, x, y):
        self.x = x
        self.y = y

    # 곱셈 연산
    def mul(self):
        result = self.x * self.y
        self.display(result)  # 메서드 호출

    # 결과 출력
    def display(self, result):
        print('곱셈 = %d' % result)


obj = multiply3  # 기본 생성자
obj.data(10, 20)
obj.mul()
