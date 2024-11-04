t = int(input())
list1 = [0,31,28,31,30,31,30,31,31,30,31,30,31]

for tc in range(1,t+1):
    result = 0
    a,b,c,d = map(int,input().split())
    if a == c:
        result = d-b+1
    else:
        result = list1[a]-b+1
        for i in range(a+1, c):
            result += list1[i]
        result += d
 print(f"# {tc} {result}")
        

    