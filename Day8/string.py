#string -- Finite sequence of characters
str1 ="Hello"
str2='Welcome'
str3="""Python Learning """
print(str1, str2, str3 )

#acessing the characters in str
str1 = "Hello Welcome"
print("lenght f the str :" ,len(str1))

print("str1[0]", str1[0])
print("str1[1]", str1[1])
print("str1[2]", str1[2])
print("str1[-1]", str1[-1])
print("str1[-2]", str1[-2])
print("str1[-3]", str1[-3])
print("str1[0:5]", str1[0:5])
print("str1[2:8]", str1[2:8])

'''strings are imutable 
but they can be assigned'''

wrong = "Hallo, world!"
correct = wrong.replace('a', 'e')
print("Original string:", wrong)
print("Modified string:", correct)

#iteration in string 
letter_count = 0
for letters in "Hello_World" :
    if(letters=='l'):
        letter_count +=1
print (letter_count,"times l appears")

#string Membership 
print ("is there l in hello ? ",'l' in "Hello")
print ("Is there w in Hello ?  ",'w' in "Hello")
print ("Is there no  w in Hello ?  ",'w'not in "Hello")

#built-in fuctions 
mystr = "Hello world Weclome to python programming"
print("list(enumerate(mystr)) : ",list(enumerate(mystr)))
print("length of the string : ",len(mystr)) 

#string formatting 
#to print -- tell me, "what is your name ?"
#to print -- tell me, "what's your name ?"
print('''tell me, "what's your name ?"''')
print('''tell me, "what is your name ?" ''')

print('tell me, "what\'s your name ?')
#escaping Character -- \
#in order to print C:\Users\Administrator\Desktop\udemy\string.py ..
#use \\ 
print("C:\\Users\\Administrator\\Desktop\\udemy\\string.py")

#to print in new line 
print("This is the first line \nThis is the second line")
#for tab spacing
print ("This is a file of python \tlearning programing (tab space '\t')")
#hex representation
print("ABC in Hex \x41\x42\x43 representation '\\x41=a'")

#format() method 
#default (implict) order
s = "{} {} and {}".format("Hi","hello" , "Welcome")
print (s)
#positional argument
s="{0},{1},{2}".format("1","3","0")
print (s)
#keywords
s="{a} {b} and  {c}".format(a="A",b="B",c="C")
print (s)

#formatting number
print("the binary representation of {0} is {0:b}" .format(20))
print("the exponent representation of {0} is {0:e}" .format(20))
print("the one third  is {0:3f}" .format(1/3))


#string Method
sample = 'gOoD MoRniNG'
print(sample)
print (sample.lower() ,"The text is Converted into lowercase")
print (sample.upper() ,"The text is Converted into uppercase")
print (sample.capitalize() ,"The text is Converted into capitalized")
print (sample.find('D') ,"find D's index")
print (sample.islower() ,"--checks is it in lowercase")
sample1="good morning"
print(sample1)
print (sample1.islower() ,"--checks is it in lowercase")
sample1="GOOD MORNING"
print(sample1)
print (sample1.isupper() ,"--checks is it in uppercase")






