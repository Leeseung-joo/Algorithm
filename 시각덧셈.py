t = int(input())
for tc in range(1,t+1):
    a,b,c,d = map(int,input().split())
    i = a+c
    j = b+d
    if i >12:
        i  = i%12
    if j > 60:
        i += j // 60
        j = j%60
    print(f"#{tc} {i} {j}")
       
    