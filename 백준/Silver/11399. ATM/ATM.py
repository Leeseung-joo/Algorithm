n = int(input())
list1 = list(map(int,input().split()))
list1.sort()
total = 0
k = 0
for i in list1:
    total += i * (len(list1) - k)
    k += 1
print(total)


