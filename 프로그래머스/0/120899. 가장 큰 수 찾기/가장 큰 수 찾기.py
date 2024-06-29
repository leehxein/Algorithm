def solution(array):
    answer = []
    max_array = max(array)
    max_index = array.index(max(array))
    answer += max_array, max_index
    return answer