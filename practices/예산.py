def solution(d, budget):
    answer = 0
    d = sorted(d)
    for i in d:
        if budget // i != 0:
            answer += 1
            budget -= i
        else:
            break
        
    return answer
