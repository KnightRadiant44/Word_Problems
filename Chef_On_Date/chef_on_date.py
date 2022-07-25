T = int(input())
for tc in range(T):
    # Read integers a and b.
    (x, y) = map(int, input().split(' '))
    
    if x >= y:
        print("YES")
    else:
        print("NO")