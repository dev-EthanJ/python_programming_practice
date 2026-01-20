# 모듈 불러오기
import my_mod01

print(my_mod01.add(3, 4))
print(my_mod01.sub(5, 3))

# 모듈의 함수 불러오기
from my_mod01 import add
print(add(2, 3))

# 모듈의 모든 함수 불러오기
from my_mod01 import *
print(sub(3, 4))