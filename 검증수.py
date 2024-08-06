list1 = list(map(int,input().split()))
result = 0
for i in list1:
    result += i*i
print(result%10)