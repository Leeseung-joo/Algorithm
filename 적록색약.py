from collections import deque
n = int(input())
graph = []
for _ in range(n):
    graph.append(list((input())))
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[0]*n for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1  #방믄 표시
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny] = 1
    
    
    
    
    
    
    
    
    
cnt = 0  
cnt1 = 0 
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt += 1 
for i in range(n):
    for j in range(n):
        if graph[i][j] == "G":
            graph[i][j] = "R"
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j)
            cnt1 += 1
print(cnt, cnt1)