def dfs(i,result):
    global cnt
    if result == k:
        cnt += 1
        return
    if i == n:
        return
    dfs(i+1,result+list1[i])
    dfs(i+1,result)




t = int(input())
for tc in range(1,t+1):
    n,k = map(int,input().split())
    list1 = list(map(int,input().split()))
    cnt = 0
    dfs(0,0)
    print(f"#{tc} {cnt}")