k = int(input())
list1 = []
for _ in range(k):
    a = int(input())
    if a != 0:
        list1.append(a)
    else:
        list1.pop(-1)
print(sum(list1))