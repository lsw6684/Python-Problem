def solution(s):
    answer = ''
    test = len(s)
    if test%2==0:
        answer=(s[test//2-1]+s[test//2])
    else:
        answer=s[test//2]
    return answer
