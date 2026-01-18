class FourCal:
    # 클래스 안에 구현된 함수 : 메서드 method
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
    
a = FourCal()
b = FourCal()
a.set_data(4, 2)
b.set_data(3, 8)

print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print()
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())
    

