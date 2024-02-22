def prime(n):
    p = [True for i in range(n+1)]
    
    p_n = 2
    while (p_n**2 < n):
        if (p[p_n] == True):
            for i in range(p_n**2, n + 1, p_n):
                p[i] = False
        
        p_n = p_n + 1
    
    return p


p = prime(10)

sum = 0

for i in range(len(p)):
    if p[i] == True:
        sum += i

print(sum)
