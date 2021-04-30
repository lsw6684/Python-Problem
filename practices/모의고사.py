def solution(answers):
    answer = [0, 0, 0]
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    idx = 0
    for x in answers:
        if x == one[idx%5]:
            answer[0] += 1
        if x == two[idx%8]:
            answer[1] += 1
        if x == three[idx%10]:
            answer[2] += 1
        idx += 1
    
    result = []
    for x in range(3):
        if answer[x] == max(answer):
            result.append(x+1)
    
    return result
