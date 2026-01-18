class Family:
    # 클래스 변수
    last_name = '김'

# 클래스 변수는 유지됨
print(Family.last_name)
a = Family()
b = Family()
print(a.last_name)
print(b.last_name)
print()

# 클래스 변수 변경시 객체 모두에 적용
Family.last_name = "박"
print(Family.last_name)
print(a.last_name)
print(b.last_name)
print()

# 클래스 변수와 동일한 이름의 객체 변수 생성 가능
a.last_name = "최"
print(Family.last_name)
print(a.last_name)
print(b.last_name)