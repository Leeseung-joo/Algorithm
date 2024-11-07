t = int(input())  # 테스트 케이스 개수
for tc in range(1, t + 1):
    n = int(input())  # 농장의 크기 N
    list1 = [list(map(int, input().split())) for _ in range(n)]  # 농작물의 가치
    start, end = n//2,n//2
    total = 0

    for i in range(n):
        for j in range(start,end+1):
            total += list1[i][j]

        if i < n//2:
            start -= 1
            end += 1
        else:
            start+=1
            end -=1
        



    print(f"#{tc} {total}")
