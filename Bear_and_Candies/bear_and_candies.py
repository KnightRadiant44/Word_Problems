T = int(input())
for tc in range(T):
    # Read integers a and b.
    (a, b) = map(int, input().split(' '))

    counter = 0
    limak = 0
    bob = 0
    while True:
        print("Counter: " + str(counter))
        counter += 1 + limak
        if counter <= a:
            limak += 1
            counter += 1 + bob
            if counter <= b:
                bob += 1
                continue
            else:
                print("Limak")
                break
        else:
            print("Bob")
            break

#Link to problem: https://www.codechef.com/problems/CANDY123