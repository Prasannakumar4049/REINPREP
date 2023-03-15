"""ap=int(input("Enter no.of Adults :"))
cp=int(input("Enter no.of Child :"))
#adult = 37550.0
#child = 1/3 of adult
#ticket=cost + 7%tax
#last price = ticket - 10%

x = ap*37500
y = 37000/3
total = (x+y)
print(total)
last price = total -
print(((ap*37550.0)+(cp*37550.0/3))*1.07)*0.90)
"""



ap=int(input("Enter no.of Adults :"))
cp=int(input("Enter no.of Child :"))
total=((ap*37550.0)+(cp*3755.0))
print(total)
total1=total*0.7
total2=total+total1
print("With Service Tax= ",total2)
fp=total2 * 0.90
print(fp)
