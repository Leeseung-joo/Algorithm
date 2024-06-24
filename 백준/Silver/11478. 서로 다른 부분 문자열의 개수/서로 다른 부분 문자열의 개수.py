a = input()
total = set()
for i in range(len(a)):
    for j in range(i,len(a)):
        total.add(a[i:j+1])
print(len(total))