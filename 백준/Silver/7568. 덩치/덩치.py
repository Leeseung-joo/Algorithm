n = int(input())
list1 = []
ans = []
for i in range(n):
    list1.append(list(map(int,input().split())))
for i in range(n):
    count = 0
    for j in range(n):
        if list1[i][0]<list1[j][0] and list1[i][1] < list1[j][1]:
            count += 1
    ans.append(count+1)
for l in ans:
    print(l,end = ' ')