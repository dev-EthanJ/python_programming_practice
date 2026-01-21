# 메모장 만들기
# 기능: 메모 추가, 메모 조회
# 입력: 메모 내용, 실행 옵션
# 출력: memo.txt

# python memo.py -a "Life is too short"
import sys

option = sys.argv[1]

if option == "-r":
    # 메모 읽기
    with open("memo.txt", "r") as f:
        print(f.read())

elif option == "-a":
    # 메모 추가
    text = sys.argv[2]

    with open("memo.txt", "a") as f:
        f.write(text)
        f.write('\n')
else:
    print("잘못된 옵션입니다.")



