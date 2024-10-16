import sys
from collections import deque
input = sys.stdin.readline
# 노드의 개수와 간선의 개수 입력
v,e = map(int,input().split())
# 모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0]*(v+1)
graph = [[]for _ in range(v+1)] # 각 노드에 연결된 간선 정보를 담기 위한 연결리스트

for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree += 1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1, v+1):
        if indegree ==0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for g in graph[now]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    #위상 정렬 수행한 결과 출력
    for res in result:
        print(res, end = ' ')
topology_sort()