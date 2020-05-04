for row in range(7):
    for col in range(4):
        if (row == 0 and col%3 != 0) or (col==3 and row%3 != 0 ) or (col == 0) or (row == 3 and col%3 !=0) or (row == 6 and col%3 !=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''
            