def solution(rsp):
    s = ''
    for i in rsp:
        if i == '2':
            s += '0'
        elif i == '0':
            s += '5'
        elif i == '5':
            s += '2'
    return s