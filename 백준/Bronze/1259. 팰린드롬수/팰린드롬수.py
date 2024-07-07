while(1):
    tag = 0
    a = input()
    if a == "0":
        break
    if a[0] == "0":
        print("no")
        continue
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            tag = 1
            continue
    if tag == 1:
        print("no")
    else:
        print("yes")
            
    