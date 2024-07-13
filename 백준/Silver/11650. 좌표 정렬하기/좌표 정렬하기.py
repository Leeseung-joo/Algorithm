import re
n = int(input())

list1 = []
for i in range(n):
    a,b = map(int,input().split())
    list1.append((a,b))
list1.sort()
for j in list1:
    list2 = str(j)[1:-1]
    result = re.sub(',', '', list2)
    print(result)