def solution(start_num, end_num):
    num_list = []
    for i in range(start_num, end_num-1, -1):
        start_num -= 1
        num_list.append(i)
    return num_list