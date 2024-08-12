import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
graph = []
visited=[[0]*n for _ in range(n)]
cnt, cnt1 = 0,0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(input().strip()))

def dfs(x,y):
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if graph[nx][ny] == graph[x][y]:
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt += 1
for i in range(n):
    for j in range(n):
        if  graph[i][j] == "G":
            graph[i][j] = "R"
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i,j)
            cnt1 += 1
print(cnt, cnt1)