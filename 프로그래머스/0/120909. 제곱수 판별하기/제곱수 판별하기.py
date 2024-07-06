def solution(n):
    s = n ** 0.5
    if n ** 0.5 == int(s):
        return 1
    elif n ** 0.5 != int(s):
        return 2