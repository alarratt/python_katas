def solution(number):
    answer=0
    for i in range(number):
        if i%3==0 or i%5==0:
            answer += i
    return(answer)
        

solution(7)