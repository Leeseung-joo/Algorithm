t = int(input())
for tc in range(t):

    n = int(input())
    list1 = list(map(int,input().split()))
    result = []
    for j in list1:
        result.append(abs(j))
    min_value = 1000001
    cnt = 0
    for k in result:
        if min_value >= k:
            min_value = k

    for a in list1:
        if a == min_value:
            cnt += 1
    print(f"# {min_value} {cnt}")
