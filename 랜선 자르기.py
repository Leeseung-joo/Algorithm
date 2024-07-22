import sys
input = sys.stdin.readline
k,n = map(int,input().split())
list1 = []
for i in range(k):
    list1.append(int(input()))
    
start,end = 1,max(list1)
while(start <= end):
    mid = (start+end)//2
    cnt = 0
    
    for line in list1:
        cnt += line //mid
        
    if cnt>=n:
        start = mid + 1
    else:
        end = mid -1
print(end)