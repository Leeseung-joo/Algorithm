import sys
from collections import deque #내풀이
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
#정답 풀이
from collections import deque 
#deque는 스택과 큐 둘다 사용 가능
def find_last_card(N):
    queue = deque(range(2,N+1))
    
    while len(queue)>1:
        queue.popleft()
        queue.append(queue.popleft())
    return queue[0]
N = int(input())
print(find_last_card(n))
