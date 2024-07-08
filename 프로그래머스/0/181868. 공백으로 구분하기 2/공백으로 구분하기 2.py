def solution(my_string):
    my_string2 = my_string.split(' ')
    answer = []
    for i in range(len(my_string2)):
        if my_string2[i] != '':
            answer.append(my_string2[i])
    return answer