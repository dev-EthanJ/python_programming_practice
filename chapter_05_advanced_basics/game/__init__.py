# __init__.py 파일의 사용

# 패키지 내 모듈을 미리 import
from .graphic.render import render_test

# 패키지 변수 및 함수 정의
VERSION = 3.5

def print_version_info():
    print(f'The version of this game is {VERSION}')

# 패키지 초기화 실행 코드
print("Initializing game...")