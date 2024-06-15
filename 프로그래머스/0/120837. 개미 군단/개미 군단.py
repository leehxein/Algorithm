def solution(hp):
    general = 5
    solider = 3
    worker = 1

    ant_cnt = 0
    ant_cnt += hp // general
    ant_cnt += hp % general // solider
    ant_cnt += hp % general % solider
    
    return ant_cnt