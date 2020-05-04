num = int(input("Enter the number-> "))
sum = 0 
for i in range(1,num+1):
    sum = sum + (1/i)
    if(i==1):
        print("1 ",end = "")
    elif(i == num):
        print("+ 1 /",i,end=" ")
    else:
        print("+ 1 /",i,end=" ")
        