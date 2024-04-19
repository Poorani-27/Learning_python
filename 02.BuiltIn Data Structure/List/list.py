'''
List : ordered collection of elements 
mutable 
can store heterogeneous data 
enclosed in [] and elements are separeted by , '''

#creating list 
a=[1,2,3,4,5] # homogeneous list ---all the elements in the list are of same type
print ("Homogeneous list" ,a,  type(a) )
print(f"Type of elements in the list : '1' :{type(a[0])} \n'2' :{type(a[1])} \n '3' :{type(a[2])}\n'4' :{type(a[3])}")
print("---------------------------------------------------------------------------------------------------------------")
a=[1,"ram",'s',True,5.009,1000223 ] # heterogeneous list ---all the elements in the list are of different types
print ("Heterogeneous list" ,a,  type(a) )
print(f"Type of elements in the list : '1' :{type(a[0])} \n'ram' :{type(a[1])} \n 's' :{type(a[2])}\n'True' :{type(a[3])}\n'5.009' :{type(a[4])}\n'1000223' :{type(a[-1])}")
print("---------------------------------------------------------------------------------------------------------------")
print("Getting list as input")
a=list(map(int, input("Enter numbers separated by space ").split()))
print(a)
x = input(" Enter elements separated by space ").split() #getting input and then storing it in list type 
a =list(x)
print(a) 
print("---------------------------------------------------------------------------------------------------------------")
print ("Built-in function")
a = [1,4,9,0,4,3,2,44,33,22,111,334,9,44,222,111,0]
print("list :",a)
print("length :",len(a))
print("maximum element :",max(a))
print("minimum element : ",min(a))
print("sum : ",sum(a))
print("sorted :",sorted(a))
print("reversed : ",list (reversed(a)))
print("any :",any(a))
print("all :",all(a))
print("enumerate : ",list (enumerate(a)) ,"Index starts from 0")
print("Count of 4 : ",a.count(4))
b=a.copy()
print("coping a to b : ",b)
print("---------------------------------------------------------------------------------------------------------------") 

print("list methods")
a = [1,4,9,0,4,3,2,44,33,22,111,334,9,44,222,111,0]
print(a)

print("Accessing : printing the second element in the list :  ",a[1])
a.append("kavi")
print("Adding a element ' kavi 'at last : ",a)
a.insert(2,"tamil")
print("Adding 'tamil' at index 2 : " ,a)
a1=["a",'d','g','g','r']
print(a)
print(a1)
a.extend(a1)
print("List1 + list2 : " , a)
a3=[0,0,0,0,0,0,0,0,22]
print("another list :",a3)
a=a+a1+a3 
print("adding list1+list2+list3 ",a)
a.remove('tamil')
print("Removing 'tamil' from the list ",a)
a.remove('kavi')
print("Removing 'kavi' from the list ",a)
a.pop()
print("pop the last element : ",a)
print("length :",len(a))
del a[3:17]
print("deleting the element from 3 rd index to 17th index ",a)
print("length :",len(a))
print("Hetergeneous list : ",a)
number=[]
string=[]
for i in a :
    if isinstance (i,int):number.append(i)
    elif isinstance(i,str):string.append(i)
print(f"Number : {number}\t string: {string}")
number2 =[12,99,33,88,55,00,22,9944,223344]
print("Number2 list : ",number2)
number.extend(number2)
print("num list +num2 list: ", number)
number.sort()
print("Sorting : ", number)
number.reverse()
print("reverse sorting : ",number)
print("string list :",string)
string.clear()
print("string cleared : ",string)
print("---------------------------------------------------------------------------------------------------------------") 

'''list comprehension : List comprehension ia a way to create a new list by applying expression to each item in the iterables like tuple ,set,range'''
print("List comprehension : '[experession  for item in iterables]")
square_value = [i**2 for i in range (0,21)]
print("list of square values using the exp i **2",square_value)
a= [1,2,3,4,8,9,22,88,99]
print("list ",a)
new_list =[i *10 for i in a ]
print("Multiplying 10 to each element : ",new_list)
'''A generator expression in Python is similar to a list comprehension, but it produces values on-the-fly instead of creating a list in memory all at once. It's more memory-efficient for large datasets because it generates values one at a time, as needed'''
print ("generator expression ")
new_list =(i *10 for i in a )
print("Multiplying 10 to each element : ",new_list)
print(next(new_list))
print(next(new_list))
print(next(new_list))

print("---------------------------------------------------------------------------------------------------------------") 
a=[i for i in range (0,21)]
print("list : ",a )
print("filtering")
even = list(filter(lambda x : x%2==0,a))
print("even numbers : ",even)
odd = list(filter(lambda x : x%2!=0,a))
print("even numbers : ",odd)

print("---------------------------------------------------------------------------------------------------------------") 
print("Reducing")
from functools import reduce
a=[1,2,3,4,5,6,7,8]
print("list",a)
product=reduce(lambda x,y: x*y,a)
print("product : ",product)  

print("---------------------------------------------------------------------------------------------------------------") 
print("mapping")
print("list :",a)
a1=list(map(lambda x : x*2,a))
print("Increasing each element*2",a1)

a=["apple","papaya","banana","orange","cherry"]
a.sort()
print(a)
a.reverse()
print(a)
a=["apple","papaya","banana","orange","cherry"]
print(a)
a.sort(reverse=True)
print(a)
a=["apjw","p","banaeeww","or","chey"]
a.sort(key=len)
print(a)
