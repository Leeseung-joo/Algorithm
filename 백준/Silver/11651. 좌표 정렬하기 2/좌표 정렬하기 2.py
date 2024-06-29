
n = int(input())

list1 = []
for i in range(n):
    a,b = map(int,input().split())
    list1.append([b,a])
list2 = sorted(list1)
for j in range(n):
    print(list2[j][1],list2[j][0])