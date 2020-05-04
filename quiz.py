C = 0
def generateNext(C):
    print(C)

    
C=float(input("please input starting series"))

s = float(input("end for your series"))

d = C

print(d)

for i in range(1,10):
    
    C = C + s
    
    print(generateNext(C))
