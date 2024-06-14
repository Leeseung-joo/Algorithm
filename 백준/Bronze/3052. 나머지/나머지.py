item = []
for i in range(10):
    item.append(int(input()))
list1 = []
for i in item:
    list1.append(i % 42)
list(set(list1))
print(len(list(set(list1))))
