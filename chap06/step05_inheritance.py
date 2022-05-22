# (1) 부모 클래스
class Super:
    # 생성자 : 동적멤버 생성
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 메서드
    def display(self):
        print('name : %s, age : %d' % (self.name, self.age))
        sup = Super('부모', 55)
        sup.display()  # 부모 멤버 호출


# (2) 자식 클래스
class Sub(Super):  # 클래스 상속
    gender = None  # 자식 멤버

    # (3) 생성자
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # (4) 메서드 확장
    def display(self):
        print('name : %s, age : %d, gender : %s' % (self.name, self.age, self.gender))


sub = Sub('자식', 25, '여자')
sub.display()  # 자식 멤버 호출


# (1) 부모 클래스
class Parent:

    # 생성자 : 객체 + 초기화
    def __init__(self, name, job):
        self.name = name
        self.job = job

    # 멤버 함수(method)
    def display(self):
        print('name : {}, job : {}'.format(self.name, self.job))


# 부모 클래스 객체 생성
p = Parent('홍길동', '회사원')
p.display()


# (2) 자식 클래스
class Children(Parent):  # Parent 클래스 상속
    gender = None  # 자식 클래스 멤버 변수 추가

    # (3) 자식 클래스 생성자
    def __init__(self, name, job, gender):
        # 부모클래스 생성자 호출
        super().__init__(name, job)  # name, job
        self.gender = gender  # 자식 멤버변수 초기화

     #  멤버 함수(method)
    def display(self):  # 함수 재정의
        print('name : {}, job : {}, gender : {}'.format(self.name, self.job, self.gender))


# 자식 클래스 객체 생성
chil = Children("이순신", "해군 장군", "남자")
chil.display()