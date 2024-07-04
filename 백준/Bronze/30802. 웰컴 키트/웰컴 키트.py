n = int(input())
list1 = list(map(int,input().split()))
t,p = map(int,input().split())
list2 = []
list2.append(t)
cnt = 0
for i in range(len(list1)):
    if list1[i] == 0:
        continue
    elif (list1[i] < list2[0]) or list1[i] == list2[0]:
        cnt += 1
    else:
        if (list1[i] % list2[0]) != 0:
            cnt += list1[i] // list2[0] + 1
        else:
            cnt += list1[i] // list2[0]
k = n // p
l = n % p
print(cnt)
print(k, l)
 