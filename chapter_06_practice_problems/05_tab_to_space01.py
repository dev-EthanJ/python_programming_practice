# 문서 파일을 읽어서 파일 안에 있는 Tab문자 \t를 공백문자 4개로 바꾸어 주는 프로그램
# 기능: 문서 파일 읽기, 문자열 변경하기
# 입력: Tab이 있는 문서파일
# 출력: 공백 4개로 변경된 문서파일

# python 05_tab_to_space01.py src dst
import sys

src = sys.argv[1]
dst = sys.argv[2]

try:
    with open(src, "r") as f_src:
        with open(dst, "w") as f_dst:
            for line in f_src:
                this_line = line.replace("\t", " " * 4)
                f_dst.write(this_line)
except FileNotFoundError as fnf:
    print("파일을 찾을 수 없습니다.")
except Exception as e:
    print(f"Error: {e}")

