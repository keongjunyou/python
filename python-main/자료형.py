# 정수형 (Integer)
# 1. 정수형으로 표현할 수 있는 데이터의 범위
a = 123456789012345678901234567890
print(a)

# 2. python 정수형과 다른 언어의 정수형의 차이
a = 2**100
print(a)

# 3. 정수형의 불변성(Immutability) 을 메모리 할당 관점에서 이해
a = 100
print(id(a))   # 주소값 : 140716738252680
a += 1
print(id(a))   # 주소값 : 140716738252712


# 실수형 (Floating-Point)
# 1. 실수형의 불변성(Immutability) 을 메모리 할당 관점에서 이해
b = 1.5
print(id(b))   # 주소값 : 2268006272112
b += 1.7
print(id(b))   # 주소값 : 2268003090256

# 2. 정밀도 및 오차 : 정밀도 한계 측면에서의 특징 (부동 소수점 연산에서 계산 오류가 발생하는 이유)
c = 0.1 + 0.2
print(c)       # 0.30000000000000004 같이 오차 발생

# 3. 부동 소수점 타입(float) 계산 오류 해결하기 위해 보다 정확한 소수점 연산을 지원하는 자료형
from decimal import Decimal
c = Decimal('0.1') + Decimal('0.2')
print(c)       # 0.3

# 4. 정확한 소수점 연산을 위해 사용되는 라이브러리의 문제
from datetime import datetime
start_time = datetime.now()
c = Decimal('0.1') + Decimal('0.2')
# d = 0.1 + 0.2    # 소요 시간 : 0:00:00.001000
print(f"result: {c} , exec time : {datetime.now() - start_time}")    # 소요 시간 : 0:00:00.000611

# f 문자열 포맷팅
name = "Python"
age = 30
height = 180
fstring = f"Name: {name}, Age: {age}, Height: {height}"
print(fstring)

# 원시 타입과 참조 타입의 차이점 (원시 타입)
x = 5
y = x
y = 10
print(x)                # 5

# 원시 타입과 참조 타입의 차이점 (참조 타입)
list1 = [1, 2, 3]
list2 = list1
list2.append(4)
print(list1)            # [1, 2, 3, 4]

# 원시 타입과 참조 타입의 메모리 공간 사용 (원시 타입)
x = 42
print(id(x))            # 140733719283784

# 원시 타입과 참조 타입의 메모리 공간 사용 (참조 타입)
my_list = [1, 2, 3]
print(id(my_list))      # 2627633853440
