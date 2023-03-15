def fun1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
fun1(10,20,30,40)

def fun1(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
fun1(10,"20",30,40)

#Keyword argument
def fun2(num1,num2,num3,num4):
    print("num1=",num1,"num2=",num2,"num3=",num3,"num4=",num4)
fun2(num4=10,num3=20,num2=30,num1=40)
fun2(num3=10,num1=20,num4=30,num2=40)

#Default Argument
def fun3(name,rollno,branch,collagename):
    print(name,rollno,branch,collagename)
fun3("Sanjuuu",296,"CSE","GIETU")
fun3("Litu",45,"CSE","GIETU")

def fun4(name,rollno,branch,collagename="GIETU"):
    print(name,rollno,branch,collagename)
fun4("Sanjuuu",296,"CSE")
fun4("Litu",45,"CSE")

def fun5(name,rollno,branch="CSE",collagename="GIETU"):
    print(name,rollno,branch,collagename)
fun5("Mitra",12)
fun5("Sanju",296,"CSE")
fun5("Litu ",45,"CST")

#Overloading
def fun6(*var):
    for i in var:
        print(i,end=' ')
fun6(1,2,3)
print()
fun6(1,2,3,4)
print()
fun6(1,2,3,4,5)
print()

def add(*var):
    sum=0
    for i in var:
        sum=sum+i
    return(sum)
print(add(10,2))
print(add(10,2,3))
print(add(10,2,3,4))

