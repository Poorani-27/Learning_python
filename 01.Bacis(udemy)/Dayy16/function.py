#Function is a block of organized reusable code that is used to perform a single related action it provide better modularity to a program and a high degree of freedom to reuse the existing quotes.
def printme(str):
    print(str)
    return
printme('abd')
printme('123')

def function(a,b):
    return (a+b)
num = function(1,2)
print(num)

#paramater passing
def changeme (mylist):
    print (id(mylist))
    print("values",mylist)
    mylist[2]=40
    print("values",mylist)
    return
mylist=[1,2,3,4,5,6,6,7,8,5]
changeme(mylist)
print(mylist)
print(id(mylist))

def changeme (mylist):
    mylist=[10,10,101,101,101,10110]
    print (id(mylist))
    print("values",mylist)
    mylist[2]=40
    print("values",mylist)
    return
mylist=[1,2,3,4,5,6,6,7,8,5]
changeme(mylist)
print(mylist)
print(id(mylist))


#Required arguments or the arguments passed to a function in correct positional order the number of arguments in the function call should match exactly with the function definition.

'''def fun(str):
    print(str)
fun() #positionalargument error.'''

#Keywords are related to the function calls when you use a keyword argument in function call the caller identifies the argument by the parameter name.

#keyword

def printn(name,age):
    print(name,age)
printn('kavi',20)
printn(age = 20 ,name ='kavi')

#default arguments
def sum(a,b):
    return(a+b) #return statement
sum1 =sum(1,2)
print(sum1)

def printinfo(name , age=20):
    print("name :",name)
    print(age ,"age")
person1 = printinfo("tamil")
person2 =printinfo("kavi",18)

#ANonymous function
#Use the Lambda Keyword to create small anonymous functions these functions are called as anonymous because they are not declared in the standard manner by using the def keyword lambda form can take any number of arguments but return chest on a value in the form of expression it cannot contain command or multiple expressions it cannot be a direct call to print because Lambda requires an expression it have their own Local namespace and cannot access variables other than those in the parameter lists and those in the global namespace.

sum=lambda arg1,arg2,arg3 :arg1+arg2+arg3
print(sum (1,2,3))

#scope of variable 
#The scope of variable determines the portion of the program where you can access a particular identifier there are two basic scopes of variable in python global variable and local variable variables that can be defined inside a function body have a local scope and those define outside have a global scope local variables can be accessed only inside the function in which they are declared global variables can be accessed throughout the program body by all the functions.
total = 10 #global variable
def func_(a,b):
    total=a+b
    print(total,"inside")
    return total
sum = func_(1,4)
print(total,"outside")
    