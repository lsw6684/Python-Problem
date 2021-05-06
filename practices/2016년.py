def solution(a, b):
    answer = ''
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    day = [31,29,31,30,31,30,31,31,30,31,30,31]
    return week[(sum(day[:a-1])+b)%7-1]
