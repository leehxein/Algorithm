def solution(n):
    n_list = []
    answer = 0

    for i in str(n):
        n_list.append (i)

    for i in n_list:
        answer += int(i)

    return answer 