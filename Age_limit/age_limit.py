T = int(input())
for tc in range(T):
    # Read integers a and b.
    (x,y,a) = map(int, input().split(' '))
    if a >= x and a < y:
        print("YES")
    else:
        print("NO")
range(T)

#Link to the problem: https://www.codechef.com/problems/AGELIMIT