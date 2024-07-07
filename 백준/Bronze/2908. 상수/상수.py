a,b = map(int,input().split())
reversed_a = "".join(reversed(str(a)))
reversed_b = "".join(reversed(str(b)))
if (reversed_a) > (reversed_b):
    print(reversed_a)
else:
    print(reversed_b)