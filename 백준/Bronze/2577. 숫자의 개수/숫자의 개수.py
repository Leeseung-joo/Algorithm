total = 1
for _ in range(3):
    i = int(input())
    total *= i  # 3개의 정수를 곱함
total_str = str(total)  # 숫자를 str타입으로 변환

for num in range(10):  # 0부터 9까지
    num_count = total_str.count(str(num))
    print(num_count)