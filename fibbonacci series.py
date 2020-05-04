n = int(input("Enter the number")) 

first = 0

second = 1

for i in range(n):
    
    print(first)
    
    temp = first
    
    first = second
    
    second = temp + first
   