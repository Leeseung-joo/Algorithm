import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split()) #노드,간선의 개수 입력받기
start = int(input())   #시작 노드 번호를 입력받기
graph = [[] for i in range(n+1)] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기

visited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int,input.split()) #a에서 b번 노드로 가는 비용이 c라는 의미임
    graph[a].append((b,c))
    
def get_smallest_node():  #방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
    min_value = INF
    index = 0 #가장 최단거리가 짧은 노드(인덱스)
    for i in range(1,n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index
def dijkstra(start):
    distance[start] = 0  #시작지점,거리는 0임
    visited[start] = True #방문처리
    for j in graph[start]:
        distance[j[0]] = j[1]   #a지점에서 b로 갈때 거리는 c이다.
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now]+j[1]
            
            if cost <distance[j[0]]:
                distance[j[0]] = cost
                    
dijkstra(start)

for i in range(1,n+1):
    if distance[i] ==INF:
        print("INF")
    else:
        print(distance[i])

 