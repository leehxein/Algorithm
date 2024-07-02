def solution(num_list):
    odd_num = ''
    even_num = ''
    for i in num_list:
        if i % 2 == 0:
            odd_num += str(i)
        elif i % 2 == 1:
            even_num += str(i)
    answer = int(odd_num) + int(even_num)
    return answer
