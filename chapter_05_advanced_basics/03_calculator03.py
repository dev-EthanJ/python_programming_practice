# 클래스 class 를 활용한 계산기 만들기
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result
    
calc1 = Calculator()
calc2 = Calculator()

print(calc1.add(3))
print(calc1.add(5))
print(calc2.add(8))
print(calc2.add(1))