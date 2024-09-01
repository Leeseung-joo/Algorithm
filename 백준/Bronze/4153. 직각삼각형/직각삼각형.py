while(1):
    a,b,c = map(int,input().split())
    list1 = []
    list1.append(a)
    list1.append(b)
    list1.append(c)
    if list1.count(0) == 3:
        break
    list1.sort()
    a,b,c = list1[0],list1[1],list1[2]
        

    if (((a*a)+(b*b) == (c*c))):
        print("right")
    else:
        print("wrong")