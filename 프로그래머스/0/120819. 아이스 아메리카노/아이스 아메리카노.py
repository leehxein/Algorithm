def solution(money):
    answer = []
    maxCup = money // 5500
    change = money % 5500
    answer.append(maxCup)
    answer.append(change)
    return answer
