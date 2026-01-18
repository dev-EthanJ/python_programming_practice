class FourCal:
    # 생성자 constructor 추가
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
    

a = FourCal(4, 2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())