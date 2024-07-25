import sys
input = sys.stdin.readline


n = int(input())
list1 = []
for i in range(n):
    list1.append(list(map(int,input().split())))
list1.sort(key = lambda x : (x[1],x[0]))
cnt = 1
pre = list1[0]
for i in list1[1:]:
    if pre[1] <= i[0]:
        pre = i
        cnt += 1
print(cnt)