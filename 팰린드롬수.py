while(1):    #처음 내 풀이:n^2
    tag = 0
    a = input()
    if a == "0":
        break
    if a[0] == "0":
        print("no")
        continue
    for i in range(len(a)//2):
        if a[i] != a[-1-i]:
            tag = 1
            continue
    if tag == 1:
        print("no")
    else:
        print("yes")

# while(True):   -->답지 풀이, 여기서 핵심은 문자열 슬라이싱이다.
#     a = input()    [start:stop:step], step의 값에 따라 역순 출력, 2칸씩 건너뛰기 등이 가능하다.
#     if a == "0": 
#         break
#     elif a == a[::-1]:
#         print("yes")
#     else:
#         print("no")

            
    