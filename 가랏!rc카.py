t = int(input())
for tc in range(1,t+1):
    n = int(input())
    cnt = 0
    prev = 0
    for _ in range(n):
        inputs  = list(map(int,input().split()))
        if len(inputs) == 2:
            if inputs[0] == 1:
                prev += inputs[1]
            else:
                prev -= inputs[1]
                if prev <=0:
                    prev = 0
            cnt += prev
        else:
            cnt += prev
    print(f"#{tc} {cnt}")
            
                