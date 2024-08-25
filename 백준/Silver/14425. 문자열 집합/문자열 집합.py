import sys
input = sys.stdin.readline
set1 = []
cnt = 0


n,m = map(int,input().split())
for i in range(n):
    set1.append(input())
for j in range(m):
    if input() in set1:
        cnt += 1
print(cnt)