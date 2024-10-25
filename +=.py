t = int(input())
for _ in range(t):
    a,b,n = map(int,input().split())
    cnt = 0
    if a > n or b > n:
        print(0)
    else:
        a,b = min(a,b), max(a,b)
        while a <= n and b<=n:
            a += b
            cnt += 1
            if a > n:
                break
            b += a
            cnt += 1
    print(cnt)


        



