# program of selection sort
list = [56,3,2,1,78,6,0,1]
print(list)
for i in range(len(list)):
    min_val = min(list[i:])
    min_ind = list.index(min_val,i)
    list[i],list[min_ind]=list[min_ind],list[i]  
print(list)
    