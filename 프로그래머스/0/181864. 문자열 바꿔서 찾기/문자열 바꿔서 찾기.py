def solution(myString, pat):
    myString = myString.replace("A","a").replace("B","b").replace("b", "A").replace("a", "B")
    if pat in myString:
        return 1
    else:
        return 0