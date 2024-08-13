import sys
input = sys.stdin.readline
list1 = [0,1,1,1,2,2,3,4,5,7,9]
for i in range(11,101):
    list1.append(list1[i-2]+list1[i-3])
t = int(input())
for i in range(t):
    n = int(input())
    print(list1[n])