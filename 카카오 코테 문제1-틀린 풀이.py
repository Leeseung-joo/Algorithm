import sys
input = sys.stdin.readline
n,m,x = map(int,input().split()) #현재위치x
tree_height = list(map(int,input().split()))
q = int(input()) #반복 횟수
d = list(input().split())
result = 0

for i in range(q):
    if tree_height[x-1] >= m:
        result += tree_height[x-1]
        tree_height[x-1] = 0
        
    for j in range(len(tree_height)):
        tree_height[j] += 1
        
    if d[i] == "L":
        x = x-1
        if x == 0:
            x = n
    elif d[i] == "R":
        x = x+1
        if x == n+1:
            x = 1
    else:
        x = x
        
print(result)

