t = int(input())
for tc in range(1,t+1):
    n,m = map(int,input().split()) #n개의 주차공간,m대의 차량
    fee = []
    w = []
    visited = [False]*n
    wait = []
    result = 0
    for _ in range(n):
        fee.append(int(input()))
    for _ in range(m):
        w.append(int(input()))
    for i in range(2*m):
        a = int(input())
        if a>0:
            for i in range(n):
                if visited[i] == False:
                    result += fee[i]*w[a-1]
                    visited[i] = a
                    break
                if i == n-1:
                    wait.append(a)
        else:
            for q in range(n):
               if visited[q] == -a:
                   visited[q] = False
                   if len(wait) != 0:
                       b = wait.popleft()
                       
                       visited[q] = b
                       result += fee[q]*w[b-1]
                       
                       break
                       
    print(f"#{tc} {result}")                  
            

