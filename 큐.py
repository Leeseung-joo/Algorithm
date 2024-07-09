import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
d = deque()
for _ in range(n):
    command = input().split()
    if command[0] == "push":
        d.append(int(command[1]))
    elif command[0] == "pop":
        if d:
            print(d.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(d))
    elif command[0] == "empty":
        if d:
            print(0)
        else:
            print(1)
        
    elif command[0] == "front":
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)     
