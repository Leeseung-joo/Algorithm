import sys
import math
input  = sys.stdin.readline
h,w,n,m = map(int,input().split())
a = math.ceil(h/(n+1))
b = math.ceil(w/(m+1))
answer = a*b
print(answer)