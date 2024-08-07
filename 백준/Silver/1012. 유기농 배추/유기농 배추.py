import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y): #상하좌우
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        #범위 안에 있고 1이면 지나간 것을 -1로 표시하고 주변 탐색
        if (0<=nx<m) and (0<=ny<n) and graph[ny][nx] == 1:
            graph[ny][nx] = -1
            dfs(nx,ny)




t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split()) #m은 가로(열), n은 세로(행)
    graph = [[0 for _ in range(m)] for _ in range(n)]
    #배추 위치 표시
    for _ in range(k): #입력은 행,열로 들어오므로 y,x임
        x,y = map(int,input().split())
        graph[y][x] = 1
    
    cnt = 0
    for a in range(m):
        for b in range(n):
            if graph[b][a] == 1:
                dfs(a,b)
                cnt += 1

    print(cnt)