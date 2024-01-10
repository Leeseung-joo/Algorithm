n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))
def dfs(x,y):
    if x<=-1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 0:   #방문한곳이 없을때까지 방문하고, 일단 방문한 곳이 없었으면 True를 리턴
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        dfs(x+1,y)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs[i][j] == True:
            result += 1
print(result)          