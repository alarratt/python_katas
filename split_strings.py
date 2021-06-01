x="12345678"
y="1234567"


def solution(s):
    output = []
    if len(s)%2==1:
        s=s+"_"
    for i in range(0,len(s),2):
        output.append(s[i:i+2])
    return(output)


solution(x)
solution(y)       

#Another solution
import re

def solution_re(s):
    return (re.findall(".{2}", s + "_"))

solution_re(x)
solution_re(y)