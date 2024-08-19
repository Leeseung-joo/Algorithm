import sys
from collections import deque

input = sys.stdin.readline
t = int(input())

for i in range(t):
    p = input().strip()  # 명령어 문자열에서 불필요한 공백 제거
    n = int(input())
    arr = input().strip()[1:-1].split(',')

    # 빈 배열일 경우 제대로 처리
    if n == 0:
        q = deque()
    else:
        q = deque(arr)

    flag = 0  # R이 짝수면 그대로, 홀수면 뒤집힘
    for j in p:
        if j == "R":
            flag += 1
        elif j == "D":
            if len(q) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    q.popleft()  # 앞쪽에서 삭제
                else:
                    q.pop()  # 뒤쪽에서 삭제
    else:
        if flag % 2 == 0:
            print("[" + ",".join(q) + "]")
        else:
            q.reverse()
            print("[" + ",".join(q) + "]")
