# 1000 미만의 자연수에서 3의 배수와 5의 배수의 총합 구하기
sum = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
        # print(i, end=" ")

print(sum)