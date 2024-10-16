while(1):
    k = list(map(int,input().split()))
    k = sorted(k)
    a = k[0]
    b = k[1]
    c = k[2]
    if a == 0 and b == 0 and c == 0:
        break
    if a+b > c:
        if a == b == c:
            print("Equilateral")
        elif a == b or a == c or b == c:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")