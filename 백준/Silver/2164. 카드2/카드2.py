import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
card_list = [i+1 for i in range(n)]
d = deque(card_list)
while True:
    if len(d) == 1:
        break
    d.popleft()
    if len(d) == 1:
        break
    k = d.popleft()
    d.append(k)
print(d[0])
