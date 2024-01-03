n,m = map(int,input().split())
adjmatrix = [[0 for _ in range(n)] for _ in range(n)]
visited = [False for _ in range(n)]
list1 = []

for _ in range(m):
	v,u = map(int,input().split())
	adjmatrix[u][v] = 1
k = list(map(int,input().split()))

 #k = 수강하려는 과목의 개수, i,j는 각각 수강하려는 교과목

def dfs1(adjmatrix,n,v,visited,list1):
	visited[v] = True
	for w in range(n):
		if visited[w] == False and adjmatrix[v][w] == 1:
			list1.append(w)
			dfs1(adjmatrix,n,w,visited,list1)
	return list1
for q in k[1:]:
	dfs1(adjmatrix,n,q,visited,list1)
	visited = [False for _ in range(n)]
print(*set(list1)) #언패킹
	
	


