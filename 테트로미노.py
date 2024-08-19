from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
maximum = 0 

def dfs(x, y, tmp, cnt):  # ㅗ 모양을 제외한 나머지 모양 탐색
    global maximum 
    if cnt == 4:
        maximum = max(maximum, tmp)
        return  # 재귀 종료
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, tmp + graph[nx][ny], cnt + 1)
            visited[nx][ny] = False

def fy(x, y):  # 'ㅗ' 모양을 탐색
    global maximum
    tmp = graph[x][y]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            arr.append(graph[nx][ny])
    length = len(arr)
    if length == 4:
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr) + graph[x][y])
    elif length == 3:
        maximum = max(maximum, sum(arr) + graph[x][y])

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)  # DFS로 ㅗ 모양을 제외한 나머지 모양 탐색
        visited[i][j] = False
        fy(i, j)  # 'ㅗ' 모양 탐색
print(maximum)
