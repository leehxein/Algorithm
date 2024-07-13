def solution(myString):
    myString = myString.replace("a", "A")
    answer = ''
    for i in myString:
        if i != "A":
            answer += i.lower()
        else:
            answer += i   
    return answer