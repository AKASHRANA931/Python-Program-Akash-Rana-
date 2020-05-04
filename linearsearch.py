def linear(list,key):
   found = False
   for i in range(len(list)-1):
       if(key == list[i]):
           found = True
    
   if(found == True):
        print("Key is found")
   else:
        print("key is not found")           
   
    
list = [1,5,3,7,2,6]
print(list)   
key = int(input("Enter the searching key"))    
linear(list,key)