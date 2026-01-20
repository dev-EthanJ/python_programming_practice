# 오류 예외 처리 기법
# 2. try-finally문

try:
    f = open("none.txt", "r")

finally:
    f.close()