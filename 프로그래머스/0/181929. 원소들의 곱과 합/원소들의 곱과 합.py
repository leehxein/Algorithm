def solution(num_list):
    mul_num = 1

    for i in num_list:
        mul_num *= i
    
    if mul_num < sum(num_list) ** 2:
        return 1
    else:
        return 0