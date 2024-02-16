#string Operators
mystr1= "hello "
mystr2 ="World!"
#concatenation -- +
print ("str1 + str2 = " ,mystr1 ,mystr2)
#repetition == *
print ("Prints the same string 3 times : ",mystr1*3)
#slicing []
print("Print the second letter of the string hello : ",mystr1[2])
#slicing Range [1:3]
print("Print the three letters of the string hello : ",mystr1[0:3])
#raw String
print("To print",r'/n')
#String Formatting
age = 25
print ("my age %i"%age)
mark=33
print("mark in floating value %f"%mark)
print ("mark in octal  %o"%mark)
max=999999999999
print (" 999999999999 in hexadecimal in lowercase %x" %max)
print (" 999999999999 in hexadecimal in uppercase %X" %max)
print (" 999999999999 in expontent in lowercase %e" %max)
print (" 999999999999 in expontent in uppercase %E" %max)
#triple Quotes
str3 = '''\nThis is a long string that is made up of several lines and non printable characters such as
tab (\\t)and they will show up the way when  displayed new lines '(\\n)' within 
the string whether explicitly given this within the bracket or just a Variable assignment will also show up'''
print (str3)
#String Encoding Functions --decode and Encode import base 64 module 
import base64
str ="This is string Example.......wow!!!"
print ("\n" ,str)
str=base64.b64encode(str.encode('utf-8'))
print ("\nEncoded : " ,str)
str=base64.b64decode(str.decode('utf-8'))
print ("\nDecoded : " ,str ,"\n")


