def promising(x):
    for i in range(x): #인덱스가 행, row[n] 값이 열
        if row[x] == row[i] or abs(row[x]-row[i]) == x-i:
            return False                #x번째 row에서의 현재 퀸의 위치, 좌우에 잇거나 대각선에 있으면 안됨
    return True                    #각각의 행에서의 row값이 x번쨰의 row값과 같지 않으면 다음 단계 수행






def dfs(x):
    global result
    if x == n:
        result += 1
    else: #각 행에 퀸 놓기
        for i in range(n): #i는 열번호 0부터 n전까지 옮겨가면서 유망한 곳 찾기
            row[x] = i #i는 행 ->1,2,3행... |||, row[x]는 열, ----
            if promising(x): #0열에 1,2,3,4...
                dfs(x+1)






t = int(input())
for tc in range(1,t+1):
    n = int(input())
    row = [0]*n
    result = 0
    dfs(0)
    print(f"#{tc} {result}")