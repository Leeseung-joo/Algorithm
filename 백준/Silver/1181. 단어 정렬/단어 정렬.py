n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
list2 = list(set(list1))
list2.sort()
list2.sort(key=len)
for j in list2:
    print(j)