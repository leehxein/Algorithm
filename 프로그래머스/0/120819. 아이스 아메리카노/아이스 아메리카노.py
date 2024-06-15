def solution(money):
    coffee = 5500
    a = money // coffee 
    b = money % coffee

    return [a, b]