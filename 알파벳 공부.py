t = int(input())
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
         'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
         'u', 'v', 'w', 'x', 'y', 'z']

for tc in range(1,t+1):
    n = input()
    listn = list(n)
    cnt = 0
    for i in range(len(listn)):
        if listn[i] == list1[i]:
            cnt += 1
        else:
            break
    print(f"#{tc} {cnt}")