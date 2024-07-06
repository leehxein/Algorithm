def solution(num_str):
    my_str = 0
    num_list = list(num_str)
    for i in range(len(num_list)):
        my_str += int(num_list[i])
    return my_str