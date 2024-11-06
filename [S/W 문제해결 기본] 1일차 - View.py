t = 10
for tc in range(1,t+1):
    n = int(input())
    list1 = list(map(int,input().split()))
    cnt = 0
    for i in range(2,n-2):
        if list1[i]>max(list1[i-2],list1[i-1],list1[i+1], list1[i+2]) :
            cnt += list1[i]-max(list1[i-2],list1[i-1],list1[i+1], list1[i+2])
    print(f"#{tc} {cnt}")
            
                 
        