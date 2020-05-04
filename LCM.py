#write a program LCM of two numbers by define a function    
n1 = int(input("Enter the number"))
n2 = int(input("Enter the number"))
greater=0

if(n1>n2):

    greater=n1

else:

    greater=n2

def LCM(n1,n2):

    if(n1>n2):

        greater=n1

    else:

        greater=n2

while(True):

    if(greater%n1 == 0 and greater%n2==0):
        print("Lcm is: ",greater)
        break
    greater = greater+1
LCM(n1,n2)
        