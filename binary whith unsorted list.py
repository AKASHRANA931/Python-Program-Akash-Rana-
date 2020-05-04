def binary(list):
    
    print(list)
    
    key=int(input('Enter the key->')) 
    
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
        
        print("key is found index is -> ",mid)
        
    else:
        
        print("key is not found")
    



def main():
    
    list = [1,6,3,9,2,7,4,5]
    
    for i in range(len(list)):
        
        for j in range(1,len(list)):
            
            if list[j-1] > list[j]:
                
                list[j-1],list[j] = list[j],list[j-1]
                
    binary(list)          
                

if __name__ == '__main__':
    
    main()            


