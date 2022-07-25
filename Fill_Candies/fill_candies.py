import math
T = int(input())
for tc in range(T):
    (n, k, m) = map(int, input().split(' '))
    
    dawn = k * m
    hate_morning = n / dawn
    rounding = math.ceil(hate_morning)
    print(rounding)

#Link to the problem: https://www.codechef.com/submit/FILLCANDIES