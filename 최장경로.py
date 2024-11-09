T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def dfs(x, cnt):
    global result
    visited[x] = 1
    for i in node[x]:
        if visited[i]==0:
            visited[i] = 1
            dfs(i, cnt +1)
    visited[x] = 0
    if cnt > result:
        result = cnt
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    node = [[] for i in range(N+1)]
    result = 0
    for i in range(M):
        x, y = map(int, input().split())
        node[x].append(y)
        node[y].append(x)
    for i in range(1, N+1):
        visited = [0 for _ in range(N+1)]
        dfs(i,1)
    print(f'#{test_case} {result}')