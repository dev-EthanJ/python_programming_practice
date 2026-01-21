# Python Programming Practice
## Chapter 05. 파이썬 날개 달기
### 연습문제 exercise

1. 클래스 상속받고 메서드 추가하기 1

다음은 `Calculator` 클래스이다.

```python
class Calculator:
    def __init__(selt):
        self.value = 0

    def add(self, val):
        self.value += val
```

이 클래스를 상속하는 `UpgradeCalculator`를 만들고, 값을 뺄 수 있는 `minus`메서드를 추가해보자. 즉, 다음과 같이 동작하는 클래스를 만들어야 한다.

```python
cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value) # print 3 
```

Anser:

```python
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val
```
<br>

2. 클래스 상속받고 메서드 추가하기

객체변수 `value`가 100 이상의 값은 가질 수 없도록 제한하는 `MaxLimitCalculator` 클래스를 만들어 보자. `Calculator` 클래스를 상속해서 만들어야 한다. 즉, 다음과 같이 동작해야 한다.

```python
cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.vaule) # print 100
```

Answer:

```python
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100
```

<br>

3. 참과 거짓 예측하기

다음 결과를 예측해보자

```python
>>> all([1, 2, abs(-3)-3])
False
>>>chr(ord('a')) == 'a'
True
```

<br>

4. 음수 제거하기

`filter`와 `lambda`를 사용하여 리스트 `[1, -2, 3, -5, 8, -3]`에서 음수를 모두 제거해 보자.

```python
number_list = [1, -2, 3, -5, 8, -3]

number_list = list(filter(lambda x: x > 0, number_list))
print(number_list)
```

<br>

5. 16진수를 10진수로 변경하기

234라는 10진수의 16진수는 다음과 같이 구할 수 있다.
`hex(234)` 이번에는 반대로 16진수 문자열 `0xea`를 10진수로 변경해보자.

```python
int("0xea", 16)
```

<br>

6. 리스트 항목마다 3 곱하여 리턴하기

`map`과 `lambda`를 사용하여 `[1, 2, 3, 4]`리스트의 각 요솟값에 3이 곱해진 리스트를 만들어보자.

```python
num_list = [1, 2, 3, 4]
new_list = list(map(lambda x: x * 3, num_list))

print(new_list)
```

<br>

7. 최댓값과 최솟값의 합

다음 리스트의 최댓값과 최솟값의 합을 구해보자.
`[-8, 2, 7, 5, -3, 5, 0, 1]`

```python
num_list = [-8, 2, 7, 5, -3, 5, 0, 1]
total = min(num_list) + max(num_list)

print(total)
```

<br>

8. 소수점 반올림하기

17/3의 결과는 다음과 같다. 
```python
>>> 17 / 3
5.6666666666666667
```

위와 같은 결괏값을 소숫점 4자리까지만 반올림하여 표시해보자

```python
print(round(17 / 3, 4))
```

<br>

9. 디렉터리 이동하고 파일 목록 출력하기

os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.

> 1. `C:\doit` 디렉터리로 이동한다
> 2. `dir`명령을 실행하고 그 결과를 변수에 담는다
> 3. `dir`명령의 결과를 출력한다.

```python
import os

os.chdir("C:\doit")
f = os.popen("dir")
print(f.read())
```

<br>

10. 파일 확장자가 .py인 파일만 찾기

`glob`모듈을 사용하여 `C:\doit` 디렉터리의 파일 중 확장자가 `.py`인 파일만 출력하는 프로그램을 작성해보자.

```python
import glob

print(glob.glob("C:\doit\*.py"))
```

<br>

11. 날짜 표시하기

`time` 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력해보자.

`YYYY/MM/DD HH:MM:SS`

```python
import time

print(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
```

<br>

12. 로또 번호 생성하기

`random` 모듈을 사용하여 로또 번호(1 ~ 45 사이의 숫자 6개)를 생성해보자. 단, 중복된 숫자가 있으면 안된다.

```python
import random

print(random.sample(range(1, 46), 6))
```

<br>

13. 누나는 영철이보다 며칠 더 먼저 태어났을까?

영철이 누나의 생일은 1995년 11월 20일이고, 영철이의 생일은 1998년 10월 6일이다. 영철이 누나는 영철이보다 며칠 더 먼저 태어났을까?

```python
import datetime

sis = datetime.date(1995, 11, 20)
bro = datetime.date(1998, 10, 6)

days_gap = bro - sis
print(days_gap.days)
```

<br>

14. 기록순으로 정렬하기

`(이름, 100m 달리기 기록(초))` 튜플을 요소로 가지는 1학년 3반 학생들의 리스트를 만들고 기록순으로 정렬해보자. 학생 수는 20명이다. 기록은 10초 이상 18초 미만이다.

```python
from faker import Faker
from operator import itemgetter

data = []
generator = Faker('ko-KR')

for i in range(20):
    name_score = (
        generator.name(),
        generator.pyint() % 8 + 10 + (generator.pyint() % 100) / 100)

    data.append(name_score)

result = sorted(data, key=itemgetter(1))

print(result)
```

<br>

15. 청소 당번 2명 뽑기

다음 4명의 학생 중 청소 당번 2명을 뽑을 수 있는 경우의 수를 모두 나열하시오.

`['성지혜', '윤성민', '김지현', '나정숙']`

```python
from itertools import combinations

student_list = ['성지혜', '윤성민', '김지현', '나정숙']

print(list(combinations(student_list, 2)))
```
        
<br>

16. 문자열 나열하기

`"abcd"` 문자열을 나열하는 경우의 수를 모두 출력하시오.

```python
from itertools import permutations
import functools

str_list = list(permutations("abcd", 4))
result_list = []

for string_set in str_list:
    this_string = functools.reduce(lambda a, b: a + b, string_set)
    result_list.append(this_string)

print(result_list)
```

<br>

17. 5명에게 할 일 부여하기

`["강승현", "이진호", "김춘자", "김예준", "박현주"]` 5명에 대해 다음 3가지의 할 일을 지정해라. `["청소", "빨래", "설거지"]`  
5명을 무작위로 섞어 앞의 3명에게 차례로 해야 할 일을 지정하고 나머지 2명에게는 "휴식"을 지정할 수 있는 프로그램을 작성하시오.

```python
from random import sample
from itertools import zip_longest

people = ["강승현", "이진호", "김춘자", "김예준", "박현주"]
chores = ["청소", "빨래", "설거지"]

new_people = sample(people, 5)
people_chores = zip_longest(new_people, chores, fillvalue="휴식")

print(list(people_chores))
```

<br>

18. 벽에 타일 붙이기

가로의 길이는 200cm이고 세로의 길이는 80cm인 벽이 있다. 이 벽에 되도록 큰 정사각형 모양의 타일을 붙이려고 한다. 이때 붙이려는 타일 한 선의 길이와 붙이는 데 필요한 타일의 개수를 구하시오.

```python
import math

len_x = 200
len_y = 80

len_gcd = math.gcd(len_x, len_y)
print(f"타일 한 선의 길이는 {len_gcd}cm 입니다.")

num_tile = len_x / len_gcd * len_y / len_gcd
print(f"붙이는 데 필요한 타일의 개수는 {int(num_tile)}개 입니다.")
```
