def solution(n):
    pizza_cnt = 1
    while True:
        if 7 * pizza_cnt >= n:
            break
        else:
            pizza_cnt += 1
    return pizza_cnt