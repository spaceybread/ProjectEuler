from functools import cache

@cache
def fibo(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibo(n - 1) + fibo(n - 2)


sum = 0

i = 0
while True:
    if len(str(fibo(i))) > 999:
        print(i)
        break
    i+= 1
