a = [4,5,1,3,2,7,6,9,1]

for i in range(1,len(a)):
    key = a[i]
    j= i - 1
    
    while a[j] > key:
        a[j+1] = a[j]
        j = j - 1 
    a[j+1] = key
print(a)
        
        
    
    