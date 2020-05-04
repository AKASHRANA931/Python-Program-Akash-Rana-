for row in range(7):
    for col in range(4):
        if (row == 0 and col%3 !=0) or (col == 0 and row !=0 and row !=6) or (col==3 and row==1) or (row==5 and col==3) or (row == 6 and col%3 != 0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
            