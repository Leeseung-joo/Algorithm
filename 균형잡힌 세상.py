while True:
    str = input()
    check = [] #괄호를 체크하기 위한 배열
    answer = "yes"
    if str == ".":
        break
    for s in str:
        if s =="(" or s =="[":
            check.append(s)
        elif s == ")":
            if not len(check):
                answer = "no"
                break
            else:
                if check.pop(-1) != "(":
                    answer = "no"
                    break
        elif s == "]":
            if not len(check):
                answer = "no"
                break
            else:
                if check.pop(-1) != "[":
                    answer = "no"
                    break
        else:
            continue
    if len(check):
        answer = "no"
    print(answer)