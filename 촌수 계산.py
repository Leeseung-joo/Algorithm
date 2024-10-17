from collections import deque
n = int(input())
a,b = map(int,input().split())
m = int(input())
graph = [[]for _ in range(n+1) ]
for _ in range(m):
    x,y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(start,target):
    q = deque()
    q.append(start)
    visited = [-1]*(n+1)
    visited[start] = 0
    
    while q:
        current = q.popleft()

        if current == target:
            return visited[current]
        for i in graph[current]:
            if visited[i] == -1: #방문하지 않은 노드만
                visited[i] = visited[current] + 1
                q.append(i)
    return -1

result = bfs(a,b)
print(result)