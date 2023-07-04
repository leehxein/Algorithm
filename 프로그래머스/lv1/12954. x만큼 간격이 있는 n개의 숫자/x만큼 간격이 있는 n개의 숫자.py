def solution(x, n):
    answer = []
    xx = x
    for i in range(n):
        answer.append(x)
        x += xx
    return answer