t = int(input())
for tc in range(1,t+1):
    n,m,k = map(int,input().split())
    list1 = list(map(int,input().split()))
    list1.sort()

    result = "Possible"
    for i in range(n):
        boong = (list1[i]//m)*k -(i+1)
        if boong <0:
            result = "Impossible"
            break
    print(f"#{tc} {result}")