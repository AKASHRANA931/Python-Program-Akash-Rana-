for row in range(9):
    for col in range(5):
        if (row == 0 and col%4 != 0) or (row == 4 and col%4 != 0) or (row != 0 and col == 0) or (row!=0 and col == 4 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()