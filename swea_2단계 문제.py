t = int(input())
for tc in range(1, t + 1):
    a, b = map(int, input().split())
    list_a = list(map(int, input().split()))
    list_b = list(map(int, input().split()))
    max_sum = 0
    
    if b > a:
        for i in range(b - a + 1):
            total = 0
            for k in range(a):
                total += list_a[k] * list_b[i + k]
            if max_sum < total:
                max_sum = total
    else:
        for i in range(a - b + 1):
            total = 0
            for k in range(b):
                total += list_b[k] * list_a[i + k]
            if max_sum < total:
                max_sum = total
                
    print(f"#{tc} {max_sum}")
