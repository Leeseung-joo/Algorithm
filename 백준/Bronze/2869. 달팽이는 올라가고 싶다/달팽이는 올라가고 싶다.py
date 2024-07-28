import math
a,b,v = map(int,input().split())
result = (v-b) / (a -b)
print(math.ceil(result))