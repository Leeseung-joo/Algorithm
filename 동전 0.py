import sys
input = sys.stdin.readline
n,k = map(int,input().split())
list1 = []
for _ in range(n):
    list1.append(int(input()))
list1.sort(reverse = True)
cnt = 0
for i in list1:
    if k == 0:
        break
    if k // i >= 1:
        cnt += k // i
        k = k % i

print(cnt)