import heapq
import sys

input = sys.stdin.readline
inf = int(1e9)

n,m,start = map(int,input().split())
graph = [[]for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
distance = [inf] * (n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z)) #1차원 리스트이므로 x번 노드에서 y번 노드로 가는 비용은 z임
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if distance[now] < dist: #now까지 가는 최단거리를 dist로 만듬
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))
dijkstra(start)

count = 0
max_distance = 0
for d in distance:
    if d != inf:
        count += 1
        max_distance = max(max_distance, d)
    
print(count -1, max_distance)
    
        