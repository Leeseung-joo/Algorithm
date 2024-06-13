list1 = list(map(int,input().split()))
list2 = [1,1,2,2,2,8]
real_list = []
for i in range(0,6):
    k = list2[i] - list1[i]
    real_list.append(k)
for i in real_list:
    print(i,end = " ")