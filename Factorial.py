n=int(input('enter the number'))
temp = n
fact = 1
while temp > 0:
    fact *= temp
    temp -= 1
print("factorial of ",n,'is',fact)
    
    