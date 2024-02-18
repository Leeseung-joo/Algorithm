import heapq
import sys
input = sys.stdin.readline #더 빠르게 동작하는 거로 바꿈
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int(input().split()))
    graph[a].append((b,c)) #a에서 b까지 가는 거리는 c이다.
    
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start)) #리스트 q에 거리를 기준으로 삽입, 튜플의 첫번째 요소를 기준으로 최소힙으로 정렬됨
    distance[start] = 0 #시작지점을 기준으로의 거리, 시작점이니깐 거리는 0
    while q: #큐가 비어있지 않으면
        dist,now = heapq.heappop(q) #가장 최단거리가 짧은 노드에 대한 정보 꺼내기, (거리,노드)
        if distance[now] < dist:
            continue
        for i in graph[now]: #현재 노드에서 다른 노드로 가는 경우가 있는만큼
            cost = dist + i[1] #시작점에서 now까지 가는 거리 dist + b까지 가는거리 c를 더함
            if cost < distance[i[0]]: #시작점에서 b까지 가는거리인 distance[i[0]]보다 다른 노드를 거쳐 b까지 가는거리가 더 짧으면 업데이트해줌.
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0])) #i[0]지점까지 가는데 cost만큼 걸림
dijkstra(start)

for i in range(1,n+1):
    if distance[i] == INF:
        print("infinity")
    else:
        print(distance[i])
     
    

