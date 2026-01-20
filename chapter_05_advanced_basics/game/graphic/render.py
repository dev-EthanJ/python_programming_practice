# sound 디렉터리의 echo.py 모듈 사용
# from game.sound import echo
# relative 하게 import
from ..sound import echo

def render_test():
    print("render")
    echo.echo_test()