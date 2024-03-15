def solution(s):
    answer = len(s)
    for step in range(1,len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step,len(s),step):
            if prev == s[j:j+step]: #이전상태와동일하다면
                count += 1
            else: #다른 문자열이 나왔다면
            compressed += str(count) + prev if count>= 2 else prev #3항연산, count가 2이상이면 붙이고 아니면 그냥 prev
            prev = s[j:j+step]
            count = 1
        compressed += str(count) + prev if count >= 2 else prev
        
        answer = min(answer, len(compressed))
    return answer