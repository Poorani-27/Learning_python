#Loop control statements
'''Loop control statements change execution 
from normal sequence when execution leaves
a scope all automatic objects in the cope 
or destroyed python supports
continue break Pass'''

'''Break --terminates the loop statement 
and transfers the execution to the statement
immediately following the loop'''

''''Continue --causes the loop to skip the
remainder of its body and immediately retest 
its condition prior to reiterating'''

'''Pass-- statement in python used when a s
tatement is required syntactically
but you dont use '''

#break 
for letter in "python":
    print(letter)
    if letter == "t":
        break
print("over")

var=10
while var>0:
    print("value : ",var)
    var =var -1
    if var == 5:
        break
print ("over")    

id=[1,2,3,4,5,6,7,8,9,0]
print(id)
x = int(input("Enter a number : "))
for i in range (len(id)):
    if x==id[i]:
        break
if i < len(id)-1:
    
    print("Found at " , i+1)
else:
    print("not found")   
    
#continue statement
for letter in "python":
    if letter == "h":
        continue
    print(letter)
        
print("over--leaves h")

pwd =123
while(True):
    x=int(input("enter password : "))
    if x!=pwd:
        print("Enter again ")
        continue
    print("entered correctly")
    break

#pass statement
def my_function():
    # TODO: Add implementation later
    pass
'''The function does nothing for now,
but it won't raise an error.'''
my_function()

#for-else 
count =0 
for i in range (11):
    print(f"hello {i}")
else :
    print("more than 10")
