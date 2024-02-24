def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

def choose(n, k):
    num = fact(n)
    denom = fact(n - k) * fact(k)

    return int(num/denom)

print(choose(40, 20))
