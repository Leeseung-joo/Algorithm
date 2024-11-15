t = int(input())
for tc in range(1,t+1):
    n = int(input())
    list1 = []
    for _ in range(n):
        a,b = map(int,input().split())
        list1.append((a,b))

    cnt = 0
    for i in range(0,len(list1)-1):
        a,b = list1[i][0], list1[i][1]
        for j in range(i+1,len(list1)):
            if a > list1[j][0]:
                if b < list1[j][1]:
                	cnt +=1
            else:
            	if b> list1[j][1]:
                	cnt += 1
    print(f"#{tc} {cnt}")
            
        
        