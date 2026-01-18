# 한 프로그램에서 2대의 계산기가 필요할 때
result1 = 0
result2 = 0

def add1(num): # 계산기1
    global result1
    result1 += num
    return result1

def add2(num): #계산기2
    global result2
    result2 += num
    return result2

print(add1(3))
print(add1(4))
print()
print(add2(7))
print(add2(3))