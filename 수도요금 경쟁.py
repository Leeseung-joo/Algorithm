t = int(input())
for tc in range(1,t+1):
    p,q,r,s,w = map(int,input().split())
    a_sum = p*w
    if w <= r:
        b_sum = q
    else:
        b_sum  = q+ (w-r)*s

    print(f"#{tc} {min(a_sum, b_sum)}")