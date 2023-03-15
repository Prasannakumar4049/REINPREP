num =int(input("Enter a number :"))
print(num,type(num))
if (num % 3 == 0 and num %5==0):
    print("Multiple of 3 and 5")
elif(num % 5 == 0):
    print("Multiple of 5")
elif(num % 3==0):
    print("Multiple of both 3 ")
else:
    print("None")
    
