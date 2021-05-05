def solution(n):
    answer = 0
    three = []
    while n > 0:
        three.append(n % 3)
        n = n //3
    three.reverse()
    for x, y in enumerate(three):
        answer += y*3**x
    return answer
