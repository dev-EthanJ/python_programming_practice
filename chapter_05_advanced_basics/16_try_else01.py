# 오류 예외 처리 기법
# 4. try-else문
try:
    age = int(input('나이를 입력하세요: '))
# Error 발생시 실행
except:
    print('입력이 정확하지 않습니다.')
# Error 발생하지 않으면 실행
else:
    if age <= 18:
        print("미성년자입니다.")
    else:
        print("성인입니다.")