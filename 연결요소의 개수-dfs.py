def find(n):
    global visited
    visited[n] = 1
    stack = []
    stack.append(n)
    while stack:
        a = stack.pop()
        for i in graph[a]:
            if not visited[i]:
                visited[i] = visited[a] + 1
                stack.append(i)








import sys
N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
visited = [0]*(N+1)
for _ in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
result = 0
for i in range(1,N+1):
    if not visited[i]:
        find(i)
        result += 1
print(result)
