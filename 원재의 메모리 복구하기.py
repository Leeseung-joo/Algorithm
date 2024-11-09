t = int(input())
for tc in range(1,t+1):
    n = input()
    list1 = []
    cnt = 0
    for _ in range(len(str(n))):
        list1.append(0)
    for i in range(len(str(n))):
        if str(n) == "".join(map(str,list1)):
            break
        if int(n[i]) == 1:
            if list1[i] == 0:
                cnt += 1
                for j in range(len(str(n))-i):
                    list1[len(str(n))-1-j] = 1
        else:
            if list1[i] == 1:
                cnt += 1
                for k in range(i,len(list1)):
                    list1[k] = 0
        
    print(f"#{tc} {cnt}")

    
