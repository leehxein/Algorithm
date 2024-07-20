def solution(a, b):
    c = str(a) + str(b)
    answer = 0
    if int(c) > 2*a*b:
        answer += int(c)
    else:
        answer += 2*a*b
    return answer