obj = open("open.txt",'r')
line = obj.readline()
while line!="":
    print(line,end='')
    line = obj.readline()
