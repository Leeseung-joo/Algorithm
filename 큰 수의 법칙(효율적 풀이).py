n,m,k = map(int,input().split())   #5 8 3
data = list(map(int,input().split()))

data.sort()
first = data[n-1]
second = data[n-2]


result = 0  #반복되는 수열의 길이가 k+1임
count = (m//(k + 1))*k
count += m % (k+1)

result += count*first + (m-count)*second
print(result)