import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().strip().split())
graph  = [list(input().strip()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
    
def bfs(x,y,visited):
    global cnt
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = True 
                if graph[nx][ny] == "O":
                    q.append((nx,ny))
                elif graph[nx][ny] == "X":
                    continue
                else:
                    q.append((nx,ny))
                    cnt += 1

    
    





for i in range(n):
    for j in range(m):
        if graph[i][j] == "I":
            bfs(i,j,visited)
            break
if cnt == 0:
    print("TT")
else:
    print(cnt)
        
            
    