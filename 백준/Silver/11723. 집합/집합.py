import sys
input = sys.stdin.readline
m = int(input())
s = set()
for _ in range(m):
    k = input().split()
    if k[0] == "add":
        if k[1] in s:
            continue
        else:
            s.add(k[1])
    elif k[0] == "remove":
        if k[1] not in s:
            continue
        else:
            s.remove(k[1])
    elif k[0] == "check":
        if k[1] in s:
            print(1)
        else:
            print(0)
    elif k[0] == "toggle":
        if k[1] in s:
            s.remove(k[1])
        else:
            s.add(k[1])
    elif k[0] == "all":
        s = {"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20"}
    else:
        s.clear()
