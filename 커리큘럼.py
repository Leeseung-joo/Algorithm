from collections import deque
import copy

v = int(input()) 
indegree = [0]*(v+1) #모든 노드에 대한 진입차수 0으로 초기화
graph = [[]for _ in range(v+1)] #각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
time = [0] * (v+1)
for i in range(1,v+1):
    data = list(map(int,input().split()))
    time[i] = data[0] #첫번째 입력정보는 강의시간에 관한것
    for x in data[1:-1]: #첫번째수와 마지막수를 제외한 번호는 선수과목 즉, 진입차수에 관련된 내용임.
        indegree[i] += 1 #i에 대한 진입차수 1증가
        graph[x].append(i) #간선 정보 추가
        
def topology_sort():
    result = copy.deepcopy(time)
    q = deque()
    
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i],result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
                
    for i in range(1,v+1):
        print(result[i])
        
topology_sort()
    