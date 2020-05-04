# program of Recurtion factorial
def factotial(n):
   
    if n == 1:
        return 1
    return n * factorial(n-1)
n = int(input("Enter the numebr"))
print(factorial(n))

    




















