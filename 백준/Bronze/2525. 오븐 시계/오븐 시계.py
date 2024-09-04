a,b = map(int,input().split())
c = int(input())
if (b+c) >= 60:
    for i in range(int((b+c)/60)):
        a += 1
        if a == 24:
            a = 0
    bun = (b+c) % 60
else:
    bun = b + c
print(a,bun, end = ' ')
