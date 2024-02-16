#dictionary
# comma separated pairs of key and value enclosed in curly braces each key is separated from its value by a colon empty dictionary without any items is written just to curly braces
#Kids are unique within a dictionary while values may not be the values of the dictionary can be of any type keys must be of immutable data type such as strings numbers or tupels.
#Dictionary is not a python sequence so obviously we cannot use the index or slice operator to access the particular value from the dictionaryInstead of that in if you want to find out the values of corresponding to a particular key all we have To do is to use the square bracket and inside write the name of the key so for the instance if you want to access the value corresponding to the key

dictionary = {'name': 'kavi','age': 20,'skill':'python'}
print(dictionary,type(dict))
print("Name ",dictionary['name'])
print(dictionary.keys() , dictionary.values())
dictionary.clear()
print(dictionary,"cleared")
dictionary['Title'] = 'student'
print(dictionary,"added one item")
# del dictionary
# print(dictionary)

#properties 
#values have no restriction
''' 
1. They can any arbitary python objects ,either standard obj or user defined objects.
2.however same is not true for the keys
3.More than one entries perky not allowed
4.When do cricket keys encountered during assignment the last assignment wins,
5.Keys must be immutable strings numbers or dupils  strings numbers or tuples as dictionary as dictionary keys '''

#built in function 
dict2={'name': 'kavi','age': 20,'skill':'python' , 'title ': 'student'}
print(dict2)
print(len(dict2),"length")
s = str(dict2)
print(s)
print(type(dict2))

#dictionary methods
#dict.clear -removes all the elements
#dict.copy()--clone created (shallow copy)
#dict.fromkeys()--creates new dic with key from seq and values set to value
#dict.get(key,default=None)--for key, returns values
#dict.items()--returns a list of dict
#dict.keys()--keys
#dict.values()--values
#dict.setdefault(key,default = None)
#dict.update(dict2)

# Creating a sample dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}

# Method 1: dict.clear()
# Removes all elements from the dictionary
original_dict.clear()
print("After clear():", original_dict)  

# Method 2: dict.copy()
# Creates a shallow copy of the dictionary
original_dict = {'a': 1, 'b': 2, 'c': 3}
copied_dict = original_dict.copy()
print("Copied Dictionary:", copied_dict)  

# Method 3: dict.fromkeys(seq, value)
# Creates a new dictionary with keys from seq and values set to the specified value
keys = ['x', 'y', 'z']
default_value = 0
new_dict = dict.fromkeys(keys, default_value)
print("New Dictionary from keys:", new_dict)  # 

# Method 4: dict.get(key, default=None)
# Returns the value for the specified key, or default if the key is not found
value_a = original_dict.get('a', 'Key not found')
value_d = original_dict.get('d', 'Key not found')
print("Value for 'a':", value_a)  
print("Value for 'd':", value_d)  

# Method 5: dict.items()
# Returns a list of dict's (key, value) tuple pairs
items = original_dict.items()
print("Items in the Dictionary:", items)  

# Method 6: dict.keys()
# Returns a list of dictionary keys
keys_list = original_dict.keys()
print("Keys in the Dictionary:", keys_list) 
