list1 = []
for i in range(9):
    list1.append(int(input()))
a = max(list1)
print(a)
print(list1.index(a)+1)