# 함수의 실행시간을 측정하는 기능 구현, Decorator 사용
import time

# 기존 함수를 parameter로 받음
def time_check(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = original_func(*args, **kwargs)
        end = time.time()

        print(f"함수 수행 시간: {end - start:.06f}초")
        return result
    return wrapper

def add(a, b):
    print(f"Add {a} and {b}")
    print(f"Result: {a + b}")

@time_check
def print_msg(msg):
    print(f"'{msg}'를 출력합니다.")

decorated_add = time_check(add)
decorated_add(3, 4)
print_msg("You need python.")
