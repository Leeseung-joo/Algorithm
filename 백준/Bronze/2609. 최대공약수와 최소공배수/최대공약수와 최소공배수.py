a,b = map(int,input().split())
def gcd(a,b): #최대 공약수
    while b > 0:
        a,b = b, a % b
    return a
def lcm(a,b):
    return a * b // gcd(a,b)
print(gcd(a,b))
print(lcm(a,b))