list1 = list(range(1,10001))
dn = []
for n in list1:
    for k in str(n):
        n += int(k)
    if n <= 10000:
        dn.append(n)
for y in set(dn):
    list1.remove(y)
for j in sorted(list1):
    print(j) 
    