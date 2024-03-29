from collections import deque

v,e = map(int,input().split())

indegree = [0] * (v+1) #모든 노드에 대한 진입차수는 0으로 초기화
graph = [[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b) #정점 a에서 b로 이동 가능
    indegree[b] += 1
    
def topology_sort():
    result = []
    q = deque()
    
    for i in range(1,v+1): #노드 중에서 진입차수가 0인 노드를 큐에 삽입
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                q.append(i)
                
    for i in result:
        print(i,end = ' ')
topology_sort()               
