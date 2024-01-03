class Node:  
	def __init__(self,v):
		self.vertex = v
		self.next = None
from collections import deque
Q = deque() #비어있는 큐
n,m = map(int,input().split())
adjlist1 = [None] * n
parent = [-1] * n
distance_sum = 0

visited = [False for _ in range(n)]
for _ in range(m):
	u,v = map(int,input().split())
	node = Node(v)
	node.next = adjlist1[u]
	adjlist1[u] = node
	node = Node(u)
	node.next = adjlist1[v]
	adjlist1[v] = node
start = int(input())

def bfs(G,n,u,parent,distance):
	visited[u] = True
	distance[u] = 0
	Q.append(u)
	while Q:#큐가 비어있지 않은경우
		v = Q.popleft()
		node = G[v]
		while node is not None:
			w = node.vertex #node.vertex는 현재 정점과 연결된 간선이 도달하는 정점
			if not visited[w]:
				visited[w] = True
				distance[w] = distance[v] + 1
				Q.append(w)
				parent[w] = v
			node = node.next


distance = [-1] * n
bfs(adjlist1, n, start, parent, distance)


max_distance = max(distance)
distance_list = [i for i, d in enumerate(distance) if d == max_distance]

if any(not visited[i] for i in range(n)):
	print(-1)
	exit()
print(" ".join(map(str, distance_list)))
max_distance = 0

for i in range(n):
	visited = [False] * n
	distance = [-1] * n
	bfs(adjlist1, n, i, parent, distance)
	current_max_distance = max(distance)
	if current_max_distance > max_distance:
		max_distance = current_max_distance
		



print(max_distance)
total_distance_sum = 0
for start in range(n):
	visited = [False] * n
	distance = [-1] * n
	bfs(adjlist1, n, start, parent, distance)
	total_distance_sum += sum(distance)
print(total_distance_sum // 2)



