t = int(input())
arr = []
for tc in range(1,t+1):
    n, m = map(int,input().split())
    for _ in range(n):
        arr.append(list(map(int,input().split())))
    result = 0
    for i in range(0,n-1):
        for j in range(n-1):
            result = max(result, arr[i][j]+arr[i][j+1] + arr[i+1][j] + arr[i+1][j+1])
    print(f"#{tc} {result}")
               