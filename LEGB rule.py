#LEGB rule

pi="globaly hu"  #fun ke liye global hai
def foo():
    print("localy hu") #fun ke liye encloser hai
    def fun():
        print(pi) #fun ke liye local hai
    fun()
foo()