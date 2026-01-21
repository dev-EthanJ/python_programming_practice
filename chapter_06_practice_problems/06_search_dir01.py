# 하위 디렉터리 검색하기
# 특정 디렉터리부터 시작해서 그 하위(디렉터리 포함)의 모든 파일 중 파이썬 파일(*.py)의 이름만 출력하는 프로그램
# 기능: 하위 디렉터리 조회, *.py만 출력하기
# 입력: 검색 시작 디렉터리 path
# 출력: 파이썬 파일명들
import sys
import glob
import os

def search_py(dir_path):
    try:
        # *.py 파일 출력
        py_list = glob.glob(os.path.join(dir_path, "*.py"))
        for file in py_list:
            print(file)

        # path의 하위 디렉터리 조회
        filenames = os.listdir(dir_path)
        for file in filenames:
            total_path = os.path.join(dir_path, file)
            if os.path.isdir(total_path):
                search_py(total_path)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("디렉터리 경로를 공백으로 구분하여 붙여주세요.")
    else:
        path = sys.argv[1]
        search_py(path)