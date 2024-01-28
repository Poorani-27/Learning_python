#Tuple
#Sequence of immutable python objects tuple cannot be changed unlike list it uses parenthesis whereas a list uses a square bracket, separated values between parenthesis
#M Tuple is written as 2 parentheses containing nothing containing a single value included

tuple1= "a",1,"b",8,'m'
print(type(tuple1))
print('''tuple tuple1= "a",1,"b",8,'m' with or without parantheses''' )


#Creating a Tuple
fruit_tuple = ('Apple', 'Banana', 'Orange', 'Mango', 'Grapes')

# Accessing Elements
print("Fruit at index 2:", fruit_tuple[2]) 

# Slicing
print("Sliced Tuple:", fruit_tuple[1:4])  
# Tuple Length
print("Number of Fruits:", len(fruit_tuple))

# Checking if an Item Exists
print("Is 'Apple' in the Tuple?", 'Apple' in fruit_tuple)  
# Iterating Through a Tuple
print("All Fruits:")
for fruit in fruit_tuple:
    print(fruit)

# Tuple Unpacking
first_fruit, second_fruit, *rest_of_fruits = fruit_tuple
print("First Fruit:", first_fruit)  
print("Second Fruit:", second_fruit)  
print("Rest of the Fruits:", rest_of_fruits)  
# Concatenating Tuples
more_fruits = ('Pineapple', 'Watermelon')
combined_fruits = fruit_tuple + more_fruits
print("Combined Fruits:", combined_fruits)

# Repeating Tuples
repeated_fruits = fruit_tuple * 2
print("Repeated Fruits:", repeated_fruits)

# Nested Tuple
nested_tuple = ('Red', 'Green', ('Blue', 'Yellow'))
print("Nested Tuple:", nested_tuple)

# Modifying a Tuple (Tuples are immutable, so this will raise an error)
# fruit_tuple[0] = 'New Fruit'

# Deleting a Tuple
del more_fruits
# print(more_fruits)  # This will raise an error as the tuple is deleted


#built in function
t = 1,2,4,5,7,8,9,66,99,11,-9,1000,-22
print(t)
print("Length of the tuple ",len(t))
print("max ",max(t))
print("min ",min(t))
a=[0,0,9,0,0,0,0,0]
print (a,type(a))
b=tuple(a)
print(b,type(b))