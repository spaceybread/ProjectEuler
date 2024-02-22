def col(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3 * n + 1

lengths = [0, ]

for i in range(1, 1000001):
    n = i
    c = 1
    while n != 1:
        n = col(n)
        c += 1
        
    lengths.append(c)
    

#print(lengths)
#print(lengths[13])

for i in range(len(lengths)):
    print(i, lengths[i])

print(max(lengths))
print(lengths.index(max(lengths)))
