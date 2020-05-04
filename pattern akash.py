def A():
    for row in range(9):
        for col in range(5):
            if (row == 0 and col%4 == 0) or (row == 4 and col%4 != 0) or (row != 0 and col == 0) or (row!=0 and col == 4 ):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
            
def K():
    print("\n")
    for row in range(9):
        for col in range(6):
            if(row + col == 5) or (row - col == 3) or (col == 0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
def S():
    print("\n")
    for row in range(7):
        for col in range(5):
            if(row == 0 and col%4 !=0) or (row == 1 and col%4 == 0) or (row == 2 and col == 0) or (row == 3 and col%4 !=0) or (row == 4 and col==4) or (row == 5 and col%4 ==0) or (row ==6 and col%4 !=0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
  
def H():  
    print("\n")    
    for row in range(9):
        for col in range(5):
            if (col == 0 ) or (col == 4) or (row == 4 and col%4 !=0):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
        
def main():
    
    A()
    K()
    A()
    S()
    H()

if __name__ == "__main__":
    main()
    


