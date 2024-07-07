a,b = map(int,input().split())
def gcd(a,b): #최대 공약수
    while b > 0:
        a,b = b, a % b
    return a
def lcm(a,b):
    return a * b // gcd(a,b)
print(gcd(a,b))
print(lcm(a,b))
    
# import math  math모듈에 gcd와 lcm있음.

# a, b = map(int, input().split())

# print(math.gcd(a, b))
# print(math.lcm(a, b))
    


    
    
