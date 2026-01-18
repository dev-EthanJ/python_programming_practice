class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    def set_data(self, first, second):
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
        result = self.first / self.second
        return result
    
# 클래스 상속 Class inheritance
class ZeroDivCal(FourCal):
    # 메소드 오버라이딩 method overriding
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second

new_calc = ZeroDivCal(4, 0)
print(new_calc.div())
