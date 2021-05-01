def solution(n, lost, reserve):
    tmp = []
    answer = 0
    for x in range(n + 2):
        tmp.append(0)
    for x in lost:
        tmp[x]-=1
    for x in reserve:
        tmp[x]+=1
    print(tmp)
    for x in range(len(tmp)-1):
        if tmp[x] < 0:
            if tmp[x-1] == 1:
                tmp[x] +=1
                tmp[x-1] -= 1
            elif tmp[x+1] == 1:
                tmp[x] += 1
                tmp[x+1] -= 1
    for x in range(len(tmp)-2):
        if tmp[x+1] >= 0:
            answer +=1
    return answer
