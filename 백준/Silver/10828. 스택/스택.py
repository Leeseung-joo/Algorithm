import sys
input = sys.stdin.readline


n = int(input())
stack_list  = []
for i in range(n):
    list1 = []
    list1 = list(map(str,input().split()))
    if list1[0] == "push":
        stack_list.append(list1[1])
    elif list1[0] == "pop":
        if stack_list:
            print(int(stack_list.pop()))
        else:
            print(-1)
    elif list1[0] == "size":
        print(len(stack_list))
    elif list1[0] == "empty":
        if stack_list:
            print(0)
        else:
            print(1)
    else:
        if stack_list:
            print(stack_list[-1])
        else:
            print(-1)
        
        
        
    
    
    
    
    
    
    
