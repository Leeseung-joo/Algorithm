t = input()
for tc in range(1,t+1):
    n,k = map(int,input())
    grade_list = ["A+","A0","A-", "B+","B", "B-","C+","C","C-","D0"]
    result_list = []
    for i in range(10):
        a,b,c = map(int,input().split())
        result_list.append(a*0.35+b*0.45+c*0.2)
    k_score = result_list[k-1]

    result_list.sort(resverse = True)
    div = n//10
    final_k_score = result_list.index(k_score) //div
    print(f"#{tc} {grade_list[final_k_score]}")