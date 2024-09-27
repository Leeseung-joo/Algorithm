a,b = map(int,input().split())
list1 = list(map(int,input().split()))
list2 = []
for i in range(a):
    if int(list1[i]) < int(b):
        list2.append(list1[i])
for j in list2:
    print(j,end = ' ')        