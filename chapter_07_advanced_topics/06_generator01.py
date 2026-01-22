# generator: iterator 생성 함수, yield 키워드 사용

# 함수로 generator 만들기
def square_generator():
    for i in range(1, 1000):
        result = i * i
        yield result

square = square_generator()
print(next(square))
print(next(square))
print(next(square))

# generator experssion으로 만들기
triple = (i * i * i for i in range(1, 1000))

for i in range(3):
    print(next(triple))

# Class로 같은 기능하는 iterator 구현
class SquareIterator:
    def __init__(self):
        self.data = 1

    def __iter__(self):
        return self
    
    def __next__(self):
        result = self.data * self.data
        self.data += 1
        if self.data >= 1000: raise StopIteration
        return result
    

square_iter = SquareIterator()
for i in range(3):
    print(next(square_iter))