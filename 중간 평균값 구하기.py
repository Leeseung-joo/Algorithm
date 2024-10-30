t = int(input())
for tc in range(1,t+1):
    result = 0
    value = list(map(int,input().split()))
    value.pop(max(value))
    value.pop(min(value))
    for i in value:
        result += i
    result /= 8
    result = round(result, 0)
    print(f"{tc} {result}")