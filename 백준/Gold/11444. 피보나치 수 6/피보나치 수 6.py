import sys
input = sys.stdin.readline

n = int(input())

memory = {1:1,2:1,3:2,4:3,5:5}

def Fibo(n):
  if memory.get(n):
    return memory[n]
  else:
    if n%2 == 1:
      memory[n] = (Fibo(n//2)**2+Fibo(n//2+1)**2)%1000000007
    else:
      memory[n] = (Fibo(n+1)-Fibo(n-1))%1000000007
    return memory[n]

print(Fibo(n))