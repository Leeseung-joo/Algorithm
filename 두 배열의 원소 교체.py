n,k = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a = sorted(a)
b = sorted(b) #하나를 내림차순으로해서 풀어도됨, 난 이게 더 편해서 이렇게 함


for i in range(k):
    if a[i] < b[n-1-i]:
        a[i],b[n-1-i] = b[n-1-i],a[i]
    else:
        break
print(sum(a))