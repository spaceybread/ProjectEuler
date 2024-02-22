def gcd3(a, b):
    if (b == 0):
        return abs(a)
    else:
        return gcd3(b, a % b)
        
def lcm3(a, b):
    return int((abs(a * b))/(gcd3(a, b)))

l = 1

for i in range(20):
    l = lcm3(l, i + 1)
    
print(l)
