import sys
import heapq

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    t = int(input().strip())
    min_heap = []
    max_heap = []
    entry_map = {}

    for _ in range(t):
        a, b = input().split()
        b = int(b)

        if a == "I":
            heapq.heappush(min_heap, b)
            heapq.heappush(max_heap, -b)
            if b in entry_map:
                entry_map[b] += 1
            else:
                entry_map[b] = 1

        elif a == "D":
            if b == 1:
                # 최대값 삭제
                while max_heap and entry_map[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    max_val = -heapq.heappop(max_heap)
                    entry_map[max_val] -= 1
            else:
                # 최소값 삭제
                while min_heap and entry_map[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    entry_map[min_val] -= 1

    # 최종 힙 정리
    while min_heap and entry_map[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and entry_map[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0], min_heap[0])
    else:
        print("EMPTY")
