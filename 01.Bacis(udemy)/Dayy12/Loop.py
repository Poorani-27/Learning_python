#loops
#A loop for iteration is one or more sequential statements executed repeatedly until a certain condition met python loop while loop and for loop.
#while Luke repeats a statement or a group of statement while arguing condition is true it tests the condition before executing the loop body
#Far loop executes a sequence of statements multiple times and abbreviates the code that manages the loop variable
 
 #while loop
count=0 
while count<10 : #till the condition true ,while loop executes
    count +=1
    print("count =",count)
print("over")
print("while -else loop")
#while loop else 
#Python supports to have an hills statement associated with their loop statement when the health statement is used with the while loop the L statement is executed when the condition becomes false
count=0 
while count<10 : #till the condition true ,while loop executes
    count +=1
    print("count =",count)
else :
    print(count , "is not less than 10")
print("over")


# python has the ability to iterate over the items of any sequence such as a list or a string if a sequence contains an expression list it is evaluated first then first item on the sequence is assigned to the iterating variable next the statement block is executed each item in the list is assigned to iterating variable statement block is executed until the entire sequence is exhausted.
for letter in "python" :
    print("current leter : ", letter)

a=[1,2,3,4,'a','v','h']
print(a)
print("Values in a ")
for i in a :
    print(i)

p=["python","c","c++","c#","rust" ,"go"]
for i in p :
    print("current language : ",i)

#for loop using range () function
print("upto to 5 terms")
for i in range(5):
    print(i)
print("between 6 and 20")
for i in range (6,20):
    print (i)
print("start,stop,step")
for i in range (4,40,4):
    print( i)

#for loop iterating by sequencing index
#An alternative way of iterating through each item by index of sits into the sequence itself.
print("key value ")
a={'a':'1','b':'2',"c":"4",'r':'8'}
for key,value in a.items() :
    print(key,value)
print("values")
for val in a:
    print(a[val])
print("keys")
for key in a.keys():
    print(key)

print("nested loop")
# nested loop
for i in range(0,11):
    for j in range(1,21 ):
        k=i*j
        print(f" {i}*{j} = {k}" )
        

#while loop single statement
'''flag=1 
while(flag):print ('hi')
print('over')
'''
#inifinte while loop
#Tell me becomes infinite loop if the condition never becomes false this result in a loop that never ends such a loop is called as infinite loop example client  server programming.
'''count=0 
while count<10 : #infinitely goes on as count = 0
    print("count =",count)
print("over")'''
var =1 
while var ==1:
    n=int(input("Enter a number : "))
    print("You Entered : ",n)
#press ctrl+c to stop the loop .It generates a Keyboard interrupt.
