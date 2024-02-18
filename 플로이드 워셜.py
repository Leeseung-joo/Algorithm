inf = int(1e9)

n = int(input())
m = int(input())
graph = [[inf] * (n+1) for i in range(n+1)] #2차원리스트생성

#자기 자신에서 자기자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0
            
for _ in range (m):
    a,b,c = map(int,input().split())
    graph[a][b] = c
    
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
            
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == inf:
            print("infinity", end = ' ')
        else:
            print(graph[a][b], end = ' ')
    print()
