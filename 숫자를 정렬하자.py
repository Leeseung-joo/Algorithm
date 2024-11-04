t = int(input())
for tc in range(1,t+1):
    n = int(input())
    list1 = list(map(int,input().split()))
    list1.sort()
    list1 = list(map(str,list1))
    string1 = " ".join(list1)
    print(f"#{tc} {string1}")