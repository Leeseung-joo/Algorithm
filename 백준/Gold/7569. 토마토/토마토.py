from collections import deque

m, n, h = map(int, input().split())
graph = []

# 3차원 리스트로 그래프 초기화
for _ in range(h):
    temp = []
    for _ in range(n):
        temp.append(list(map(int, input().split())))
    graph.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]  # dh -> dz로 수정

def bfs():
    q = deque()
    cnt = 0
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 1:
                    q.append((z, x, y))
                    cnt += 1
    
    if cnt == n * m * h:
        return 0
    
    while q:
        z, x, y = q.popleft()  # poplft -> popleft로 수정
        for i in range(6):
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nz < 0 or nx < 0 or ny < 0 or nz >= h or nx >= n or ny >= m:
                continue
            if graph[nz][nx][ny] == 0:
                graph[nz][nx][ny] = graph[z][x][y] + 1
                q.append((nz, nx, ny))

    max_value = -1
    for z in range(h):
        for x in range(n):
            for y in range(m):
                if graph[z][x][y] == 0:
                    return -1
                max_value = max(max_value, graph[z][x][y])
    
    return max_value - 1

result = bfs()
print(result)
