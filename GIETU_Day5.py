#Que 1
#Vehicle Premium Amount
'''
class Fun():
    def __init__(self,vehicle_id,type1,cost,pre_amount):
        self.__vehicle_id=vehicle_id
        self.__type1=type1
        self.__cost=cost
        self.__pre_amount=pre_amount

    def get_func(self):
        if(self.__type1=="two wheelers"):
            pre_amount=(2/100)*self.__cost
            
        elif(self.__type1=="Four wheelers"):
            pre_amount=(6/100)*self.__cost
        else:
            pre_amount="error"
        return pre_amount
    def set_func(self):
        print(self.__pre_amount)
    def display(self):
        print("the vehicle details are",self.__type1)
 
F1=Fun(50,"wheelers",100,0)
print(F1.get_func())
F1.display()
'''

#Que 2

'''#A university wants to automate their addmission process.
students are admitted based on marks scored in a qualifying exam.
 A student is identified by student id,age,marks in qualifying exam
data are valid,if :
        # age is greater than 20
          marks is between 0 to 100(both inclusive)
          A student qualifies for admission,if
          age and marks are valid and marks is 65 or more
----------------------------------------------------------------
Write a python program to represent the students seeking admissing in the
university
Rules to Follows:
the details of student class are given below:
Class name:student
--Attr
             student_id
             marks
             age
Methods
(public)_init_()
       create and intialize all instance  variables to none
validate_marks()
     if data is valid, return true.Else,return false
validate_age()
    check_qualification()         validate marks and age,
if valid,check if marks is 65 or more.
  variables to set its values
getter methods include getter methods for all instance
variables to get its value
continuing with the previous scenerio,
a student eligible for admissioin has to choose a courseand pay the fees for it.
if they have scored more than85 marks in qualifing exam they get 25% discount
on fees. valid course ids and fees are given below:

course id     fees
1001          25575.0
1002          15500.0
'''
'''
class Fun():
    def __init__(self,student_id,age,marks,course_id):
        self.student_id=student_id
        self.age=age
        self.marks=marks
        self.course_id=course_id
    def valid_age(self):
        if(self.age>20):
            return True
        else:
            return False
    def valid_marks(self):
        if(self.marks>=0 and self.marks<=100):
            return True
        else:
            return False
    def check_qualification(self):
        if self.validate_marks() and self.validate_age() and self.__marks>=65:
            return True
        else:
            return False
    def eligible(self):
        if(self.marks>=85 and self.marks<=100):
            return True
        else:
            return False
    def course(self,course_id):      
            if(self.course_id==1001):
                self.fees=25575.0
            if(self.course_id==1002):
                self.fees=15500.0
            return self.fees
    def discount(self):
        if(self.eligible):
            self.fees=(25/100)*self.fees
        else:
            return self.course()
m1=Fun(1001,21,89,1001)
print(m1.course(1001))
'''


'''
class Student:
    def __init__(self,s_id,age,marks):
        self.__s_id=None
        self.__age=None
        self.__marks=None

    def validate_marks(self):
        if self.get_marks() >=0 and self.get_marks()<=100:
            return 1
        return 0

    def validate_age(self):
        if self.get_age()>20:
            return 1
        return 0

    def check_qualification(self):
        if self.validate_marks() and self.validate_age() and self.get_marks()>=65:
            print(self.fees())
            return 1
        
        return 0
      
    def fees(self):
        if self.check_qualification():
            dic={"Course 1001":25575.0,"Course 1002":15500.0}
            discount={"Course 1001":25575.0*0.75,"Course 1002":15500.0*0.75}
            print("Course List::")
            if self.get_marks()<=85:
                return (dic)
            else:
                return (discount)
        else:
            return "Not eligible for any course!"

    def set_id(self,id):
        self.__s_id=id
    def get_id(self):
        return self.__s_id

    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age

    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks

s1=Student(0,0,0)

s1.set_id(int(input("ID:")))
s1.set_age(int(input("Age:")))
s1.set_marks(int(input("Marks:")))
print(s1.fees())
print("Qualified? :",s1.check_qualification())

'''

'''
class Fun():
    def __init__(self):
        self.__student_id=None
        self.__age=None
        self.__marks=None
    def set_id(self,id):
        self.__s_id=id
    def get_id(self):
        return self.__s_id
    def set_age(self,age):
        self.__age=age
    def get_age(self):
        return self.__age
  
    def set_marks(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks  
        
    def valid_age(self):
        if(self.__age>20):
            return True
        else:
            return False
    def valid_marks(self):
        if(self.__marks>=0 and self.__marks<=100):
            return True
        else:
            return False
    def course(self,marks):
        d={"CSE":2554,"MECh":2555}
        if(marks>85):
            for i in d:
                d[i]=d[i]-d[i]*0.25
            print("The course is offered to you after discount of 25%",d)
        else:
            print("The course offered to u:",d)
    def valid_qualification(self):
        if(self.__marks and self.valid_marks() and self.valid_age() ):
            self.course(self.__marks)
            return True
        else:
            return False

s1=Fun()
s1.set_id(9)
s1.set_age(21)
s1.set_marks(44)
if(s1.valid_qualification()):
    print("Admission can be done")
else:
    print("admission can not be done")

'''

'''
#Que 3
#Pizza

type=['small','medium','Small','Medium']
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name.title()
        self.__quantity=quantity
    def validate_quantity(self):
        if self.__quantity is range(1,6):
            return True
        else:
            return False
    def get_customer_name(self):
        return self.__customer_name
    def get_quantity(self):
        return self.__quantity
class Pizzaservices:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=0
        self.__service_id=None
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in type:
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_pizza_type() and Customer.validate_quantity(self.__customer):
            if self.__pizza_type.title()=="Small":
                self.pizza_cost=150*Customer.get_quantity(self.__Customer)
                if self.__additional_topping:
                    self.pizza_cost+=35*Customer.get_quantity(self.__Customer)
            if self.__pizza_type.title()=="Medium":
                self.pizza_cost=200*Customer.get_quantity(self.__Customer)
            Pizzaservices.counter+=1  
        else:
            self.pizza_cost=-1
    def get_service_id(self):
        return self.__service_id
    def get_pizza_type(self):
        return self.__pizza_type
    def get_customer(self):
        return self.__additional_topping
class Doordelivery(Pizzaservices):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        self.delivery_charges=0
        self.__distance_in_kms=distance_in_kms
        Pizzaservices.__init__(self,customer,pizza_type,additional_topping)
    def validate_distance_in_kms(self):
        if self.__distance_in_kms in range(1,11):
            return True
        else:
            return False
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservices.calculate_pizza_cost(self)
            if self.pizza_cost!=-1:
                distance=-1
                while(distance<=self.__distance_in_kms):
                    if distance in range(1,6):
                        self.pizza_cost+=5
                    if distance in range(6,11):
                        self.pizza_cost+=7
                    distance +=1
        else:
            self.pizza_cost=-1
    def get_delivery_charge(self):
        return self.get_delivery_charge
    def get_distance_in_kms(self):
        return self.get_distance_in_kms
c=Customer("Ashu",5)
p1=Pizzaservices(c,"Medium",True)
p1.calculate_pizza_cost()
print(p1.pizza_cost)
print(p1.get_service_id())

d1=Doordelivery(c,"Medium",False,6)
d1.calculate_pizza_cost()
print(d1.pizza_cost)
print(d1.get_service_id())

'''

