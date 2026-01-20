import my_mod02

# 모듈 변수 사용 가능
print(my_mod02.PI)

# 모듈 클래스 사용 가능
math = my_mod02.Math()
print(math.solv(2))

# 모듈 함수 사용 가능
print(my_mod02.add(my_mod02.PI, 4.4))

# 반지름이 5인 원의 넓이
print(math.solv(5))