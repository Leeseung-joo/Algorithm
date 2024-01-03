class Node:
	def __init__(self,v):
		self.vertex = v
		self.next = None

n,m = map(int,input().split())
adjlist1 = [None] * n
visited = [False for _ in range(n)]
list1 = []

for _ in range(m):
	v,u = map(int,input().split())
	node = Node(v)
	node.next = adjlist1[u]
	adjlist1[u] = node
k = list(map(int,input().split()))

 #k = 수강하려는 과목의 개수, i,j는 각각 수강하려는 교과목

def dfs2(adjlist1,n,v,visited,list1):
	visited[v] = True
	node = adjlist1[v]
	while node is not None:
		w = node.vertex
		if visited[w] == False:
			list1.append(w)
			dfs2(adjlist1,n,w,visited,list1)
		node = node.next
	return list1
for q in k[1:]:
	dfs2(adjlist1,n,q,visited,list1)
	visited = [False for _ in range(n)]
print(*set(list1)) #언패킹
	
	
node = Node(v)
node.next = adjlist1[u]
adjlist1[u] = node

