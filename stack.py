#By Akash Rana
list = []

print('stack->',list)
def push(): 
    
    ele = int(input("Enter the push element"))
    list.append(ele)
    print("insert successfully")
def pop_stack():
    
    if len(list)-1 <= 0:
        print("Empty stack")
    else:
        print("poped successfully")
        return list.pop()
        
        
def display():
    print("your stack element->",end="")
    for i in range(len(list)):
        print(list[i],end=" ")
        
        
        
def main():
    ch = 0
    
    while(1):
        print("\n1.push")
        print("2.pop")
        print("3 display")
        print("4.Exit")
        ch=int(input("Enter your choice -> "))
        if (ch==1):
            push()
        
        elif(ch == 2):
            pop_stack()
        
        elif(ch == 3):
            display()
            
        else:
            break
        

if __name__ == '__main__':
    
    main()
    

