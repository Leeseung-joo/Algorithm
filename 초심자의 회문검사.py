t = int(input())
for tc in range(1,t+1):
    k = input()
    flag = 0
    for i in range(len(k)//2):
        if k[i] != k[-1-i]:
            print(f"#{tc} {0}")
            flag = 1
            break
    if flag == 0:
        print(f"#{tc} {1}")



            