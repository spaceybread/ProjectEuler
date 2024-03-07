def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

s = str(fact(int(input())))

sum = 0

for i in range(len(s)):
    sum += int(s[i])

print(sum)
