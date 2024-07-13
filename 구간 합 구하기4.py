import sys
input = sys.stdin.readline

n,m = map(int,input().split())  #부분합 문제
list1 = list(map(int,input().split()))
sum_list = []
sum_list.append(0)
for i in range(0,n):
    sum_list.append(sum_list[i] + list1[i])
for i in range(m):
    a,b = map(int,input().split())
    print(sum_list[b]-sum_list[a-1]) 