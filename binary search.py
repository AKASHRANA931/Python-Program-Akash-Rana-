def binary(list,key):
   
    low=0
    high=len(list)-1
    Found = False
    while low <= high and not Found:
        mid = (low + high) // 2
        if key == list[mid]:
            Found = True
            
        elif key > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
        
    if Found == True:
        
        print("key is found ",key)
        
    else:
        print("key is not found")
    
list =[1,2,4,5,6,7,8,9]
print(list)
key=int(input('Enter the key->'))
binary(list,key)   

