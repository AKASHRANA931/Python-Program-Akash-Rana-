def Add(x,y):
	return x + y
def Sub(x,y):
	return x - y
def Mul(x,y):
	return x * y
def Div(x,y):
	return x//y

print("1.Addition")
print("2.Subtraction")
print("3.Multiplecation")
print("4.Division\n")
choice = int(input("Enter your choice->"))

x = int(input("\nEnter first number->"))
y = int(input("Enter second number->"))

if(choice== 1):
	print("Addition is->",Add(x,y))
elif(choice == 2):
	print("Subtration is->",Sub(x,y))
elif(choice == 3):
	print("multiplecation is ->",Mul(x,y))
elif(choice==4):
	print("Divisition is->",Div(x,y))
else:
	print("invelid choice")

