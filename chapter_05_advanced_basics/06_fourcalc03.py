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
class FiveCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result
    
a = FiveCal(4, 2)
print(a.pow())
print(a.add())