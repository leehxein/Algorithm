def solution(my_string, index_list):
    answer = ''
    for idx, i in enumerate(index_list):
        answer += my_string[i]
    return answer