# Python Programming Practice with "Do it! 점프 투 파이썬"
## Chapter 04. 파이썬의 입출력
### 연습문제

1. 홀수, 짝수 판별하기
- 주어진 자연수가 홀수인지, 짝수인지 판별해 주는 함수 `is_odd()`를 작성해보자. `is_odd`함수는 홀수이면 `True`, 짝수이면 `False`를 리턴해야 한다.

```python
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False
```

<br>

2. 모든 입력의 평균값 구하기
- 입력으로 들어오는 모든 수의 평균값을 계산해주는 함수를 작성해보자. 단, 입력으로 들어오는 수의 개수는 정해져 있지 않다.

```python
def avg_number(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

avg_numbers(1, 2) # 1.5
avg_numbers(1, 2, 3, 4, 5) # 3.0
```

<br>

3. 프로그램 오류 수정하기 1
- 다음은 2개의 숫자를 입력받아 더한 후에 리턴하는 프로그램이다.

```python
input1 = input("첫 번째 숫자를 입력하세요.: ")
input2 = input("두 번째 숫자를 입력하세요.: ")

total = input1 + input2
print(f'두 수의 합은 {total}입니다.')
```

프로그램의 오류를 수정하세요.

```python
input1 = int(input("첫 번째 숫자를 입력하세요.:"))
input2 = int(input("두 번째 숫자를 입력하세요.:"))

print(f'두 수의 합은 {input1 + input2}입니다.')
```

<br>

4. 출력 결과가 다른 것은?

```python
print('you' 'need' 'python')
print('you' + 'need' + 'python')
print('you', 'need', 'python')
print("".join(['you', 'need', 'python']))
```

- `print('you', 'need', 'python')`은 `you need python`으로 출력되고, 나머지는 `youneedpython`으로 출력된다.

<br>

5. 프로그램 오류 수정하기 2
- 다음은 파일(`test.txt`)에 `"Life is too short"` 문자열을 저장한 후 다시 그 파일을 읽어 출력하는 프로그램이다.

```python
f1 = open("test.txt", "w")
f1.write("Life is too short")

f2 = open("test.txt", "r")
print(f2.read())
```

- 예상한 값이 출력되도록 프로그램을 수정해보자.

<br>

```python
f1 = open("test.txt", "w")
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", "r")
print(f2.read())
f2.close()
```

<br>

6. 사용자의 입력 저장하기

- 사용자의 입력을 파일(`test.txt`)에 저장하는 프로그램을 작성해보자. 단, 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고 새로 입력한 내용을 추가해야 한다.

```python
user_input = input("저장할 내용을 입력하세요.: ")
f = open("test.txt", "a")
f.write(user_input)
f.write('\n')
f.close()
```

<br>

7. 파일의 문자열 바꾸기
- 다음과 같은 내용을 지닌 `test.txt`가 있다. 이 파일의 내용 중 `"java"`라는 문자열을 `"python"`으로 바꾸어 저장해 보자.

```
Life is too short
you need java
```

```python
f = open("test.txt", "r")
body = f.read()
f.close()

body = body.replace("java", "python")
f = open("test.txt", "w")
f.write(body)
f.close()
```

<br>

8. 입력값을 모두 더해 출력하기

- 다음과 같이 실행할 때 입력값을 모두 더해 출력하는 스크립트를 작성해 보자.
```
C:\doit> python myargv.py 1 2 3 4 5 6 7 8 9 10
55
```

```python
import sys
args = sys.argv[1:]
total = 0
for i in args:
    total += int(i)

print(total)
```
