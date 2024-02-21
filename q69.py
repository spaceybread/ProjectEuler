from sympy.ntheory.factor_ import totient

out = [0, 0, 0 ]

n = 1000000

for i in range(3, n):
    #print(i)
    out.append(i / totient(i))

print(max(out), out.index(max(out)))
