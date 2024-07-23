import sys
input = sys.stdin.readline
case = int(input())

for _ in range(case):
    n,m = list(map(int,input().split()))
    list1 = list(map(int,input().split()))
    
    index = [i for i in range(n)] #문서들의 기존 순서 저장
    cnt = 0
    
    while True:
        if list1[0] == max(list1):
            cnt += 1
            if index[0] == m :
                print(cnt)
                break
            else:
                del list1[0]
                del index[0]
        else:
            list1.append(list1[0])
            del list1[0]
            index.append(index[0])
            del index[0]