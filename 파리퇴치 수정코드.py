t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            cnt = 0
            for a in range(i, i + m):
                for b in range(j, j + m):
                    cnt += arr[a][b]
            result = max(result, cnt)
    print(f"#{tc} {result}")
