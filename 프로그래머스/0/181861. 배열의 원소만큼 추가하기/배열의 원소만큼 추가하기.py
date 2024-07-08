def solution(arr):
    x = []
    for i in range(len(arr)):
        for j in range(arr[i]):
            x.append(arr[i])  
    return x