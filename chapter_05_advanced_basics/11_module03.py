# 다른 디렉터리에 있는 모듈 불러오는 방법

# 1. sys.path.append 사용하기
import sys

# 파이썬 라이브러리가 설치되어있는 디렉터리 목록
print(sys.path)

# 모듈 디렉터리 path 추가
sys.path.append("C:\\Users\\hello\\Documents\\python_programming_practice\\chapter_05_advanced_basics\\my_mod")

print(sys.path)

import my_mod

print(my_mod.add(3, 4))

# 2. PYTHONPATH 환경 변수 사용하기
# set PYTHONPATH=path