import heapq
import sys
input = sys.stdin.readline
heap_list = []
n = int(input())
for _ in range(n):
    item = int(input())
    if item == 0:
        if heap_list:
            print(heapq.heappop(heap_list))
            continue
        else:
            print(0)  
            continue
    if type(item) == int:
        heapq.heappush(heap_list, item)