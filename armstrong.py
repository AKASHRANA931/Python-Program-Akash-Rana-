i = int(input("Enter the number"))
#for i in range(1,n+1):
num = i
result = 0
n =len(str(num))
while(i != 0):
    digit = i % 10
    result = result + digit ** n
    i = i//10
if(num == result):
    print("number is armstrom->",num);
else:
    print("Number is not armstrom->",num);