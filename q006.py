def sum(n):
    return int(0.5 * n * (n + 1))

def sumsofsq(n):
    return int( ((2*n)/3 + 1/3) * sum(n))
    

N = 100
val = sum(N)**2 - sumsofsq(N)

print(val)
