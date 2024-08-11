from collections import deque

m,n = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    q = deque()
    cnt = 0
    
    #익은 토마토의 위치를 모두 큐에 넣음
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i,j))
                cnt += 1
    if cnt == n*m:
        return 0
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx,ny))
    max_value = -1
    for row in graph:
        for value in row:
            if value == 0:
                return -1
            max_value = max(max_value, value)
    return max_value - 1
        
    




result = bfs()
print(result)