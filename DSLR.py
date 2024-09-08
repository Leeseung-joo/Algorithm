import sys
from collections import deque

input = sys.stdin.readline
t = int(input().strip())  # 여기를 수정하여 입력을 받습니다.

for _ in range(t):
    A, B = map(int, input().strip().split())

    visited = [False for _ in range(10000)]  # 인덱스 범위 10001을 10000으로 변경
    q = deque()
    q.append([A, ""])
    visited[A] = True

    while q:
        num, command = q.popleft()

        if num == B:
            print(command)
            break

        d = num * 2 % 10000
        if not visited[d]:
            visited[d] = True
            q.append([d, command + "D"])

        s = (num - 1) % 10000
        if not visited[s]:
            visited[s] = True
            q.append([s, command + "S"])

        l = (num % 1000) * 10 + num // 1000
        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])

        r = (num % 10) * 1000 + num // 10
        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])
