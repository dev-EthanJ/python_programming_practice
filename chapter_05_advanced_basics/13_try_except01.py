# 오류 예외 처리 기법
# 1. try - except 문

try:
    4 / 0
except ZeroDivisionError as e:
    print(e)