#program of merge sort

def merge(list):
    if len(list) > 1:
        mid = len(list)//2
        left_list = list[:mid]
        right_list = list[mid:]
        merge(left_list)
        merge(right_list)
        i=  0
        j = 0
        k = 0
        while i<len(left_list) and j<len(right_list):
              
               
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i = i + 1
                k = k + 1
        
                
            else:
                   
                list[k] = right_list[j]
                   
                j = j + 1
                   
                k = k + 1
                
        while i < len(left_list):
            list[k] = left_list[i]
            i=i+1
            k=k+1
        while j<len(right_list):
            list[k] = right_list[j]
            j=j+1
            k=k+1
               
    
    
list = [1,6,2,4,9,5,7,8,3]
merge(list)
print(list)