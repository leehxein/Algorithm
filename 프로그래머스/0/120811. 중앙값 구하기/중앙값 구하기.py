def solution(array):
    array.sort() #오름차순정렬(리스트)
    idx = int(len(array) // 2)
    anwser = array[idx]
    return anwser