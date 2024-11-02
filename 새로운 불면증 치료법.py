t = int(input())
target_number = set(range(10))
for tc in range(1,t+1):
    n = int(input())

    numbers = set()
    nx, count = n,1
    while True:
        temp= set(str(nx))
        numbers.update(temp)

        if len(numbers) == 10:
            break
        count += 1
        nx = n*count
    print(f"#{tc} {nx}")
