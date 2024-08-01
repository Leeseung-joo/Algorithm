from collections import deque
n,k = map(int,input().split())
MAX = 10**5
visited = [0]*(MAX+1)
def bfs(s):
    q = deque()
    q.append(s)
    
    while q:
        current = q.popleft()
        if current == k:
            return visited[k]
        for i in (current+1,current-1,current*2):
            if 0<=i<=MAX and not visited[i]:
                visited[i] = visited[current]+1
                q.append(i)
print(bfs(n))
