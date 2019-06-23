class Cookie:
    pass

a = Cookie()
b = Cookie()

print(type(a))
print(type(b))

class FourCal: # 클래스에 함수 쓸 때는 무조건 self로 시작함.
    #first = 0
    #second = 0 선언안해도 돌아감 변수선언이 알아서 된 것. 자바는 선언해야 돌아감.
    def __init__(self, first, second): # 여기서 초기값 설정도 가능. 생성자는 객체 생성할 때 호출되어 생성된다.
        self.first = first
        self.second = second    
    
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def sub(self):
        result = self.first - self.second
        return result

    def div(self):
        return self.first / self.second
        
'''
c = FourCal()
c.setdata(5,7) # self는 무시한다.
print(c.first)
print(c.second)
'''
'''
c.first=10 # 이렇게 가능.
c.second=20
print(c.first)
print(c.second)
'''
'''
d = FourCal()
d.setdata(3,4)

print(id(c)) # 주소값 출력
print(id(d))
print(id(c.first))
print(id(d.first))

sumresult = c.add()
print(sumresult)

subresult = c.sub()
print(subresult)

mulresult = c.mul()
print(mulresult)

divresult = c.div()
print(divresult)
'''

c=FourCal(5,0)
print(c.add())

# 오버로딩 : 같은 클래스 안에서 함수 이름이 같은 것. but 매개변수 모양만 다름. 파이썬에서는 필요 없음.
# 오버라이딩 : 부모꺼 받아서 고쳐서 쓰는 것! 부모 생성자도 가져온다.

class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:  # 나누는 값이 0인 경우 0을 리턴하도록 수정
            return 0
        else:
            return self.first / self.second

d=SafeFourCal(5,0)
print(d.div())

# 클래스 변수는 클래스에서 만들어 진 변수이기 때문에 인스턴스 변수에서도 다 사용된다.
# 인스턴스 변수는 개별적으로 인스턴트마다 사용된다.

class M :
    class_V = 0

a = M()
b = M()
print(a.class_V)
print(b.class_V)

M.class_V=5 # 모든 부분이 바껴버림.
print(a.class_V)
print(b.class_V)
a.class_V=6 # 개별 부분만 바껴버림.

print(a.class_V)
print(b.class_V)