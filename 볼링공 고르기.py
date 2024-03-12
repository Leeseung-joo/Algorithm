n,m= map(int,input().split()) #개수 n,최대 무게 m
weight_list = list(map(int,input().split()))
result = 0

for i in weight_list:
    result += n - weight_list.count(i)
print(result//2)