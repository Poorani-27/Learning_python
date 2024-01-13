#string 
a= "          Tamil kavi          "  
#string function
print(a.upper())#to print all letters in uppercase
print(a.lower())#to print all the letters in lowercase
print(a.capitalize()) #to capitalize the first letter of the string
print(a.title())#to capitailize the first letter of each word in string
#following functions either return True or False :
print(a.isupper())#to check whether the letters of the string are in uppercase.
print(a.islower())#to check whether the letters of the string are in lowercase.
print(a.isalpha())#to check whether the string contains only alpha characters
print(a.isnumeric())#to check whether the string contains only numeric characters
print(a.isalnum())#to check whether the string contains both alpha and numeric characters
print(a.isdecimal())#to check whether the string is decimal
print(a.endswith("es"))#to find whether the string ends with the given characters
#count and length 
print(a.count('o'))#count the number of 'o' in the string
print(len(a)) #prints the length of the string including white spaces.
#to remove white spaces
print(len(a.strip()))#remove the white spaces at both sides
print(len(a.lstrip()))#remove only at left side
print(len(a.rstrip()))#remove only at right side
#find
print(a.find('0'))#finds the index of O in the string
print(a.find('o',5))#finds the character o that comes after the 5th index
#replace 
print(a.replace('o','s'))#replaces o with s in the string 
#split and Partition
print(a.split('.'))
print(a.splitlines())
print(a.partition("-"))

#-----------------------------------------------------------string  manipulation--------------------------------------------
#slicing
a= "sample" 
print(a[2])#prints the letter at the index two which is 'm'
print(a[0:2])#print only the starting two characters of the string as it is mentioned from index 0 t0 2 'sa'
print(a[:4])#prints from starting to index 4
print(a[-4:-1])#right to left indexing '-'
print(a[:-1])#except the last letter
print(a[::-1])#reverse of the string
#formatting
name="kavi"
age="20"
print(f"My name is {name} and I'm {age} yeras old.   --fstrings")
print("My name is %s and I am %s years old." % (name, age) ,"---% formatting")
print("My name is {} and I am {} years old." .format (name, age) ,"---format() ")
#WIdth and precision 
value = 3.14159
print(f"The value is: {value:.2f}")  # Displays the value with 2 decimal places.
#alignment
text = "Hello"
print(f"{text:>50}" )  # Right-aligned with a width of 50.
#fill and alignment
text = "Hello"
print(f"{text:*^100}")  # Center-aligned with '*' filling, width 10
#type specific formatting
number = 42
print(f"The answer is: {number:04}")  # Pads with zeros to make a 4-digit number.
