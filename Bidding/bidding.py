T = int(input())
for tc in range(T):
    listo = list(map(int, input().split(' ')))
    maxxy = max(listo)
    if listo.index(maxxy) == 0:
        print("Alice")
    elif listo.index(maxxy) == 1:
        print("Bob")
    else:
        print("Charlie")
range(T)

#Link to problem: https://www.codechef.com/problems/AUCTION