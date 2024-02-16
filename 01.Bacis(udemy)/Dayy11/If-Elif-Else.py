#Decision making
#Anticipate possible conditions occurring while execution of the program and specify instructions to be executed for each condition,
#Decision statements evaluate logical expression which produces true or false as outcomes
#Non zero and non null values are considered as true null and zero values are considered as false

#Decision making statemnts 

#If statement ----------consist of a boolean expression followed by one or more statements
#If else statement and if statement followed by an optional ill statement which executes when the Boolean expression is false
#mr dip statement one if or else if statement inside another if or else if statements.

print("If amt is greater than 1000 provide discount 10% ")
discount = 0 
amount = int(input("Enter The  amount : "))
if amount >1000 :
    discount = amount *0.10
print("discount =  " ,discount)
print ("pay {a}" .format (a=amount-discount))


#the if elif statement allows you to check multiple expressions. there Can be any number of yellow statements following an if statement elf is also optional.
print("If-Elif --if the amount is greater than 1000 provide 10% discount or if the amount is greater than 500 provide 5% discount")
 
discount = 0 
amount = int(input("Enter The  amount : "))
if amount >1000 :
    discount = amount *0.10
elif amount >500:
    discount = amount *0.05

print("discount =  " ,discount)
print ("pay {a}" .format (a=amount-discount))

#else
print("If-Elif --if the amount is greater than 1000 provide 10% discount or if the amount is greater than 500 provide 5% discount otherwise display 'No Discount ' For amount less than 500 ")
 
discount = 0 
amount = int(input("Enter The  amount : "))
if amount >1000 :
    discount = amount *0.10
    print("discount =  " ,discount)
    
elif amount >500:
    discount = amount *0.05
    print("discount =  " ,discount)
    
else :
    print("No Discount for amount less than 500")

print ("pay {a}" .format (a=amount-discount))

#Python Single Statement Suites
#If the suite of an if clause consists only of a single line, it may go on the same as the header statement
print("single statement suites ")
mark = int(input("Enter Mark : "))
if (mark >=35 ): print ("pass")
else : print("fail")