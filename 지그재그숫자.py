t = int(input())
for tc in range(1,t+1):
    n = int(input())
    result = 0
    while n!=0:
        if n%2 == 0:
            result -= n
            n -= 1
        else:
            result += n 
            n-= 1
    print(f"#{tc} {result}")
        

