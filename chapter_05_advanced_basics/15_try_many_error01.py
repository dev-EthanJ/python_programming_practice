# 오류 예외 처리 기법
# 3. 여러 개의 오류 처리하기

try:
    a = [1, 2]
    print(a[2])
    4 / 0
except (ZeroDivisionError, IndexError) as e:
    print(e)
'''
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except IndexError:
    print("인덱싱 범위를 초과했습니다.")
'''