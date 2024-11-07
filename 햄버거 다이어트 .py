def dfs(index,staste,scal):
    global max_taste
    if scal > total_cal:
        return
    if max_taste < staste:
        max_taste = staste
    
    if index == n:
        return
    taste,cal = data[index]
    
    dfs(index+1, staste+taste, scal+cal) #재료를 사용하는 경우
    dfs(index+1, staste,scal) #재료를 사용하지 않은 경우











t = int(input())
for tc in range(1,t+1):
    n, total_cal = map(int,input().split())
    data = [list(map(int, input().split())) for _ in range(n)]
    max_taste = 0
    dfs(0,0,0)
    print(f"#{tc} {max_taste}")
    
    