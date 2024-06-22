def solution(cipher, code):
    answer = cipher[code-1:len(cipher):code]
    return answer
