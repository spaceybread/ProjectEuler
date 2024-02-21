n = 1000
m = 1000

all = []

prod = "1001"


if len(prod) % 2 == 0:
    flag = True
    for i in range(int(len(prod)/2)):
        if prod[i] != prod[- (i + 1)]:
            flag = False
        
    if flag == True:
        all.append(int(prod))
    
else:
    flag = True
    for i in range(int((len(prod) - 1)/2)):
                
        if prod[i] != prod[- (i + 1)]:
            flag = False
        
    if flag == True:
        all.append(int(prod))

print(all)




while n > 0:
    n = n - 1
    m = 999
    while m > 0:
        m = m - 1
        prod = str(n * m)
        print(n, m)
        if len(prod) % 2 == 0:
            flag = True
            for i in range(int(len(prod)/2)):
                if prod[i] != prod[- (i + 1)]:
                    flag = False
        
            if flag == True:
                all.append(int(prod))
    
        else:
            flag = True
            for i in range(int((len(prod) - 1)/2)):
                
                if prod[i] != prod[- (i + 1)]:
                    flag = False
        
            if flag == True:
                all.append(int(prod))

      
all.sort()
print(all)
print(all[-1])
print(9009 in all)
