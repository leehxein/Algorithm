def solution(num_list, n):
    answer = 0
    
    for i in range(len(num_list)):
        if num_list[i] == n:
            answer += 1
    else:
        answer += 0

    if answer >= 1:
        return 1
    else:
        return 0