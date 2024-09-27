import sys
n = int(sys.stdin.readline())
result = 1
for i in range(n):
    result *= (n-i)
print(result)