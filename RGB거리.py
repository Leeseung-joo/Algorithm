n = int(input())
list1 = [0] * n
for i in range(n):
    list1[i] = list(map(int,input().split()))

for i in range(1,n):
    list1[i][0] = min(list1[i-1][1], list1[i-1][2]) + list1[i][0]
    list1[i][1] = min(list1[i-1][0], list1[i-1][2]) + list1[i][1]
    list1[i][2] = min(list1[i-1][0], list1[i-1][1]) + list1[i][2]
print(min(list1[n-1][0], list1[n-1][1], list1[n-1][2]))
    
