def prime(n):
    p = [True for i in range(n+1)]
    
    p_n = 2
    while (p_n**2 < n):
        if (p[p_n] == True):
            for i in range(p_n**2, n + 1, p_n):
                p[i] = False
        
        p_n = p_n + 1
    
    return p

p = prime(10000**2)

primes = []

for i in range(len(p)):
    if p[i] == True:
        primes.append(i)

print(primes[0], primes[1], primes[2], primes[3], primes[4], primes[5])
print(len(primes))
print(primes[10001], primes[10002], primes[10003])
