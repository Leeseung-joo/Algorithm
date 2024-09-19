

list1 = []
list2 = []
N,M = map(int,input().split())

for i in range(N):
    list1.append(input())
for j in range(M):
    list2.append(input())
set1 = set(list1)
set2 = set(list2)
set3 = set1 & set2
list3 = list(set3)
print(len(list3))
list3.sort()
for k in list3:
    print(k)