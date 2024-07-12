n = int(input())

d = [0] * (n+1) #dp 리스트
for i in range(2,n+1):
    d[i] = d[i-1] + 1 #현재 수에서 1을 빼는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1) #3가지 경우 중 가장 작은 것을 고른다.
print(d[n])    