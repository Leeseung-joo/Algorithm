t = int(input())
for tc in  range(1,t+1):
    n = int(input())
    a,b,c,d,e,f,g,h = 0,0,0,0,0,0,0,0
    if n >= 50000:
        a = n//50000
        n %= 50000
    if n >= 10000:
        b = n//10000
        n %= 10000
    if n >= 5000:
        c = n//5000
        n %= 5000
    if n >= 1000:
        d = n//1000
        n %= 1000
    if n >= 500:
        e = n //500
        n %= 500
    if n>= 100:
        f = n // 100
        n %= 100
    if n >= 50:
        g  = n // 50
        n %= 50
    if n >= 10:
        h = n //10
        n %= 10

    print(f"#{tc}")
    print(f"{a} {b} {c} {d} {e} {f} {g} {h}")