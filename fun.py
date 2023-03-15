#functions
def fun1():
    print("Function")
fun1()
def fun2(n1,n2):
    print("n1=",n1,"n2=",n2)
fun2(1,2)

#Addition
def fun3(n1,n2):
    n3 = n1+n2
    return n3
print("Value of n3=",fun3(20,30))

def fun4(n1,n2):
    n3=float(n1)+n2
    return n3
print("Value =",fun4(10,2.3))

def fun5(n1,n2):
    n3=float(n1)+n2
    return n3
print("Value =",fun5('10',2.3))
