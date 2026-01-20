# 오류 회피하기
try:
    f = open("none", "r")
except FileNotFoundError:
    pass