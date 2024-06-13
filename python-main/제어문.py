# 삼항 연산자 (조건부 표현식, conditional expression)
# 1. 삼항 연산자에 대한 기초적인 사용법
x = 10
y = 20

a = x if x > y else y
print(a)  # 20

# 2. 삼항 연산자의 가독성 높이는 케이스와 가독성 해칠 수 있는 케이스에 대해 이해
# 가독성 높이는 케이스
age = 18
status = "adult" if age >= 18 else "teen"
print(status)  # adult

# 가독성 해칠 수 있는 케이스
x, y, z = 10, 9, 8
result = "A" if (x > y and x > z) else ("B" if y > z else "C")
print(result)
