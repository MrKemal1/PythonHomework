primeNumbers=[2]
control=False
for i in range(3,101):
    for j in range(2,i):
        if i % j == 0:  
            control=False
            break
        else:
            control=True
    if control==True:
        primeNumbers.append(i)

print(primeNumbers)