import sys
input = sys.stdin.readline
n,k = map(int,input().split())
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)
    
print(factorial(n) // (factorial(n-k) * factorial(k)) )