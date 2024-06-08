N = int(input())
count = 0
for i in range(1,N+1):
    list1 = list(map(int,str(i)))
    if i < 100:
        count += 1
    elif list1[0]-list1[1] == list1[1]-list1[2]:
        count += 1
print(count)