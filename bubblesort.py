a=[8,4,1,3,2,6,9]
count = 0
for i in range(len(a)):
    for j in range (1, len(a)):
        
        if a[j-1]>a[j]:
            count+=1
            a[j-1] , a[j] = a[j] , a[j-1]
            break
print(a,count)
