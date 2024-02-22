import math

def count(n) :
    c = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) :
        if (n % i == 0) :
            if (n / i == i) :
                c += 1
            else :
                c += 2
                  
    return c

n = 2300

while True:
    tri = int(0.5 * n * (n + 1))
    
    c = count(tri)
    
    if c > 500:
        print("Solved: ", tri, c)
        quit()
    
    print(tri)
    
    n += 1
