#Declaring variables

a = 10 #a is the variable that stores the value 10
b = "Hello" # b is a string variable that holds the text Hello.

# Reassinging the variables

a = 20 # the value 10 is now changed to 20
print(a) 

# Data types 
# In Python, data types are classified into two main groups:
""" Numeric data types: includes integers (int), 
floating point numbers (float), and complex numbers (complex)
Non-numeric data types: includes strings (str), 
characters (chr), booleans """

x = 10 #integer
y = 3.5 #float
z = True #boolean - represents true or false
w = "I am a String!" #string
v = 'I am also a String!' #character

# Printing out the different data types
print("Integer: ", x)
print("Float: ", y)
print("Boolean: ", z)

#Concatenation of variables
f_name = "Tamil"
l_name = "kavi"
full_name = f_name + " " + l_name #concatenating 
print("Full Name: ", full_name)

#type() function
print(type(x))
print(type(y))
print(type(z))

#id() function
print (id(x))
print (id(y))
