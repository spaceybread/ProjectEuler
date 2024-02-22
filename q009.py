for a in range(1, 1001):
    for b in range(1, 1001):
        for c in range(1, 1001):
            if b > a and c > b:
                if a + b + c == 1000:
                    print(a, b, c)
                    if a**2 + b**2 == c**2:
                        print("Solved: ", a, b, c)
                        print(a*b*c)
                        quit()
