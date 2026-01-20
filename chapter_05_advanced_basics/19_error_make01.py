# 예외 만들기
class MyException(Exception):
    # 예외를 변수로 받아 print()할때 나올 값을 __str__() 메소드로 설정
    def __str__(self):
        return "MyException 발생"

def say_nickname(word):
    if word == "멍청이":
        raise MyException
    print(word)

try:
    say_nickname("천재")
    say_nickname("멍청이")
# except MyException:
#     print("허용되지 않는 별명입니다.")
except MyException as me:
    print(me)