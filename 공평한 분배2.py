
t = int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split())
    list1 = list(map(int,input().split()))
    min_result = 1000000000
    list1.sort()
    for i in range(n-k+1):
        temp = list1[i+k-1] - list1[i]
        min_result = min(temp, min_result)
    print(f"#{tc} {min_result}")
            