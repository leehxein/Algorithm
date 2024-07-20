def solution(a, b):
    answer = 0
    c= str(a) + str(b)
    d= str(b) + str(a)
    
    if int(c) > int(d):
        answer += int(c)
    elif int(c) < int(d):
        answer += int(d)
    else:
        answer += int(c)
    return answer