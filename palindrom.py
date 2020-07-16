n = int(input())
result = ""
for i in range(n):
    num = int(input())
    temp = num
    while(temp>0):
        digit = temp % 10
        result = result + str(digit)
        temp  = temp //10
    if(result == str(num)):
        print("Yes")
    else:
        print(result)
    result = ""

    
    