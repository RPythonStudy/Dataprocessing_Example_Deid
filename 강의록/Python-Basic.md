# [1] 핵심 요약

파이썬의 가장 큰 특징은 **가독성**과 **간결함**이며, "인생은 짧으니 파이썬이 필요하다(Life is short, you need Python)"는 철학을 바탕으로 설계되었습니다.

---

## 1. 파이썬의 주요 특징 (Key Features)

* **인터프리터 언어:** 컴파일 과정 없이 코드를 바로 실행합니다.
* **동적 타이핑 (Dynamic Typing):** 변수의 타입을 선언하지 않으며, 실행 시점에 결정됩니다.
* **들여쓰기(Indentation) 강제:** 중괄호 `{}` 대신 공백(주로 4칸)으로 코드 블록을 구분합니다. 이는 코드의 일관성을 강제합니다.
* **First-class Objects:** 모든 것(함수, 클래스 포함)이 객체로 취급됩니다.

---

## 2. 변수와 데이터 타입 (Variables & Types)

파이썬은 별도의 선언 키워드(`int`, `let`, `var` 등)가 필요 없으며, 할당과 동시에 생성됩니다.

### 개념

* **Dynamic Typing:** `a = 10` (정수) -> `a = "Hello"` (문자열)로 자유롭게 변경 가능.
* **주요 자료구조:** * `List`: `[1, 2, 3]` (Mutable, 순서 있음)
* `Tuple`: `(1, 2, 3)` (Immutable, 수정 불가)
* `Dict`: `{"key": "value"}` (Key-Value 쌍)
* `Set`: `{1, 2, 3}` (중복 없음)

### 예제

```python
# 변수 할당
age = 25
name = "Python"
is_easy = True

# 리스트와 딕셔너리
skills = ["C++", "Java", "Python"]
user_info = {
    "id": 101,
    "role": "Developer"
}

# 다중 할당 (Unpacking)
x, y = 10, 20

```

---

## 3. 함수 정의 및 호출 (Functions)

함수는 `def` 키워드를 사용하며, 반환 값의 타입을 명시할 필요가 없습니다.

### 개념

* **매개변수 기본값 (Default Arguments):** 인자가 전달되지 않을 때의 기본값 설정 가능.
* **가변 인자:** `*args`(리스트 형태), `**kwargs`(딕셔너리 형태)를 통해 개수가 정해지지 않은 인자를 받을 수 있음.

### 예제

```python
# 함수 정의
def greet(name, message="Hello"):
    return f"{message}, {name}!"

# 함수 호출
result1 = greet("Alice")           # "Hello, Alice!"
result2 = greet("Bob", "Welcome")  # "Welcome, Bob!"

# 람다 함수 (익명 함수)
add = lambda a, b: a + b
print(add(3, 5)) # 8

```

---

## 4. 제어문 (Control Flow)

파이썬의 제어문은 괄호를 생략하며 끝에 콜론(`:`)을 붙입니다.

### 개념

* **if-elif-else:** 타 언어의 `else if`가 `elif`로 축약됩니다.
* **for 루프:** 인덱스 기반이 아닌 **Iterable 객체 순회** 방식입니다.

### 예제

```python
# 조건문
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

# 반복문 (List 순회)
languages = ["Python", "Go", "Rust"]
for lang in languages:
    print(f"I like {lang}")

# range() 함수 사용
for i in range(3): # 0, 1, 2
    print(i)

```

---

## 5. 모듈 및 패키지 임포트 (Importing)

파이썬은 "Batteries Included" 철학을 가지고 있어 방대한 표준 라이브러리를 제공합니다.

### 개념

* `import 모듈`: 모듈 전체를 가져옵니다.
* `from 모듈 import 함수`: 특정 요소만 가져옵니다.
* `as`: 별칭(Alias)을 지정합니다.

### 예제

```python
import math
print(math.sqrt(16))  # 4.0

from datetime import datetime
now = datetime.now()
print(now)

import numpy as np  # 외부 라이브러리 관례적 별칭

```

---

## 6. 파이썬만의 특징적인 구문 (Pythonic Code)

다른 언어 사용자들에게 가장 생소하면서도 강력한 기능들입니다.

### 리스트 컴프리헨션 (List Comprehension)

반복문을 한 줄로 작성하여 리스트를 생성하는 기법입니다.

```python
# 일반적인 방식
squares = []
for x in range(5):
    squares.append(x**2)

# 리스트 컴프리헨션
squares = [x**2 for x in range(5)] # [0, 1, 4, 9, 16]

```

### 컨텍스트 매니저 (with 문)

파일이나 네트워크 연결 등 자원을 열고 닫는 과정을 자동으로 처리합니다.

```python
with open("test.txt", "w") as f:
    f.write("Hello World")
# 블록을 나가면 자동으로 f.close() 호출됨

```

---

# [2] 주석과 독스트링

파이썬에서 **주석(Comment)**과 **독스트링(DocString)**은 단순히 코드 설명을 넘어, 협업과 자동 문서화의 핵심입니다. 다른 언어(C-style 등)와 비교하며 핵심적인 차이를 정리해 드립니다.

---

## 1. 주석 (Comments)

파이썬은 한 줄 주석을 기본으로 하며, 타 언어의 `/* ... */`와 같은 별도의 블록 주석 기호는 없습니다.

### 핵심 개념

* **한 줄 주석:** `#` 기호를 사용합니다.
* **인라인 주석:** 코드와 같은 줄에 공백을 두 번 띄우고 작성하는 것이 PEP 8(스타일 가이드) 권장 사항입니다.
* **여러 줄 주석:** 공식적으로는 여러 줄에 `#`을 붙이는 것을 권장하지만, 실행에 영향을 주지 않는 문자열(`"""`)을 활용하기도 합니다.

### 예제

```python
# 이것은 전체 한 줄 주석입니다.
x = 10  # 이것은 인라인 주석입니다.

# 여러 줄 주석의 경우
# 보통 이렇게 한 줄씩
# 샵(#) 기호를 붙여 작성합니다.

"""
문자열 리터럴을 이용한 방식:
변수에 할당하지 않은 문자열은 인터프리터가 무시하므로
여러 줄 주석처럼 활용할 수 있습니다.
"""

```

---

## 2. 독스트링 (DocString, Documentation Strings)

독스트링은 파이썬의 객체(모듈, 클래스, 함수) 정의 첫 부분에 위치하는 특별한 형태의 문자열입니다. 단순 주석과 달리 **객체의 메타데이터**로 저장됩니다.

### 핵심 개념

* **정의:** 함수, 클래스, 모듈의 첫 번째 줄에 오는 `"""세 개짜리 따옴표"""` 문자열입니다.
* **목적:** 코드의 '사용법'을 설명합니다. (주석은 '왜 이렇게 짰는지'를 설명)
* **접근성:** 프로그램 실행 중에 `__doc__` 속성을 통해 접근하거나 `help()` 함수로 조회할 수 있습니다.

### 예제

```python
def calculate_power(base, exponent):
    """
    밑수(base)를 지수(exponent)만큼 거듭제곱한 결과를 반환합니다.
  
    Args:
        base (int): 밑수
        exponent (int): 지수
      
    Returns:
        int: 거듭제곱 결과
    """
    return base ** exponent

# 독스트링 확인 방법
print(calculate_power.__doc__) # 문자열로 출력
# help(calculate_power)        # 도움말 페이지 형식으로 출력

```

---

## 3. 주석 vs 독스트링 차이점 요약

| 구분                   | 주석 (Comment)                    | 독스트링 (DocString)                 |
| ---------------------- | --------------------------------- | ------------------------------------ |
| **기호**         | `#`                             | `""" ... """` 또는 `''' ... '''` |
| **위치**         | 코드 어디서나                     | 객체(함수, 클래스 등) 정의 바로 아래 |
| **목적**         | 개발자를 위한 코드 내부 구현 설명 | 사용자를 위한 인터페이스/API 문서화  |
| **실행 시 참조** | 불가능 (인터프리터가 무시)        | 가능 (`obj.__doc__`으로 접근)      |

---

## 4. 실무 표준 독스트링 스타일 (Google Style)

대규모 프로젝트에서는 일관성을 위해 특정 형식을 따릅니다. 가장 널리 쓰이는 **Google Style** 예시입니다.

```python
def fetch_user_data(user_id: int) -> dict:
    """사용자 ID를 받아 프로필 정보를 가져옵니다.

    Args:
        user_id: 데이터베이스에서 조회할 사용자의 고유 ID.

    Returns:
        사용자 정보가 담긴 딕셔너리. 없을 경우 빈 딕셔너리 반환.

    Raises:
        ConnectionError: 데이터베이스 연결에 실패했을 때 발생.
    """
    # ... logic ...
    pass

```

*독스트링을 잘 작성하면, IDE에서 함수 위에 마우스를 올렸을 때 위와 같이 깔끔하게 정리된 도움말 팝업을 볼 수 있습니다.*

---

# [3] 심화 교육 자료

파이썬을 실무에서 더욱 강력하게 만드는 **객체 지향 프로그래밍(OOP), 예외 처리, 그리고 파이썬만의 고급 기능(Decorator, Type Hinting)**을 정리한 심화 교육 자료입니다.

---

## 1. 객체 지향 프로그래밍 (OOP)

파이썬의 클래스는 Java나 C++와 유사하지만, `self`라는 명시적인 예약어와 동적 속성 추가가 가능하다는 점이 다릅니다.

### 핵심 개념

* **`self`**: 인스턴스 자신을 가리키는 첫 번째 매개변수입니다 (Java의 `this`와 유사).
* **`__init__`**: 생성자 메서드입니다.
* **Access Modifier**: 엄격한 `private`, `protected`는 없으며, 관례적으로 언더바(`_` 또는 `__`)를 사용해 캡슐화를 표현합니다.

### 예제

```python
class Animal:
    def __init__(self, name):
        self.name = name  # Public
        self.__age = 0    # Private (Name Mangling 발생)

    def speak(self):
        pass

class Dog(Animal): # 상속
    def speak(self):
        return f"{self.name} says Woof!"

my_dog = Dog("Rex")
print(my_dog.speak())

```

---

## 2. 예외 처리 (Exception Handling)

파이썬은 `try-except` 구문을 사용하며, 예외 발생 여부와 상관없이 실행되는 `finally` 외에도 `else` 블록을 지원합니다.

### 구조

* `try`: 로직 실행
* `except`: 에러 발생 시 처리
* `else`: 에러가 **발생하지 않았을 때만** 실행
* `finally`: 무조건 실행 (자원 해제 등)

### 예제

```python
try:
    value = int(input("숫자를 입력하세요: "))
    result = 10 / value
except ValueError:
    print("숫자만 입력 가능합니다.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
else:
    print(f"결과: {result}")
finally:
    print("작업을 종료합니다.")

```

---

## 3. 데코레이터 (Decorators)

기존 함수의 코드를 수정하지 않고 기능을 추가하거나 수정할 때 사용하는 파이썬의 강력한 기능입니다. Java의 Annotation과 비슷해 보이지만, 함수를 인자로 받아 새로운 함수를 반환하는 **고차 함수(Higher-order function)** 원리로 작동합니다.

### 예제

```python
def logger(func):
    def wrapper(*args, **kwargs):
        print(f"--- {func.__name__} 함수 시작 ---")
        result = func(*args, **kwargs)
        print(f"--- {func.__name__} 함수 종료 ---")
        return result
    return wrapper

@logger
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("World")

```

---

## 4. 제너레이터 (Generators)

모든 데이터를 메모리에 올리지 않고, 필요할 때마다 값을 생성하여 반환하는 방식입니다. 대용량 데이터 처리 시 메모리 효율이 극대화됩니다.

### 개념

* `yield` 키워드를 사용합니다.
* 함수의 상태를 유지한 채로 값을 반환하고, 다음 호출 시 중단된 지점부터 다시 실행합니다.

### 예제

```python
def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1

counter = count_up_to(5)
for num in counter:
    print(num) # 1, 2, 3, 4, 5 순차 출력 (메모리에는 한 번에 하나만 존재)

```

---

## 5. 타입 힌팅 (Type Hinting)

파이썬은 동적 타입 언어이지만, 대규모 프로젝트에서의 가독성과 정적 분석을 위해 타입을 명시할 수 있습니다. (실행 시 강제성은 없으나 도구의 도움을 받습니다.)

### 예제

```python
from typing import List, Dict

def process_data(names: List[str], scores: Dict[str, int]) -> float:
    total = sum(scores.values())
    return total / len(names)

# IDE(PyCharm, VS Code)에서 타입 체크 및 자동 완성을 지원함

```

---

### [참고] Python 클래스 구조 시각화

파이썬 클래스의 상속과 인스턴스화 과정을 이해하면 다른 언어와의 차이점을 명확히 알 수 있습니다.

---
