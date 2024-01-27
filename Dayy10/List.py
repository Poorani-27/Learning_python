#List can be written as a list of, separated values that is items between square brackets. Items in the list need not have the same type.creating a list is as simple as putting different, equal to separated values between the square brackets
lista =[1,3,'a',-3,'u',7.9,"ok", "listed","b=a"]
print ("list : \n" ,lista)

#Accessing Values In list
#To Access values in the list use the square brackets for slicing along with the index or indexes to obtain the value available at that index to obtain the value available at that index

list1 = [0,1,2,3,4,'d','b','vv']
list2 = ['i','n','a','r','i',1,0,8,4]
print("list1 = ",list1)
print("list2 = ",list2)

#update 
list1[1] = "a=bc"
list2[2] ="903993"
print ("value at index 1 of list1 changed from 1 to a=bc",list1)
print ("value at index 2 of list2 changed from a to 903993",list2)

#deleting
del list1[0] 
print ("First Value of list1 is deleted ",list1)
del list2
# print("After Deleting List2 , Tried to print list2\n")
# print(list2,"\n")

#list operations
#List respond to the + and * operations much like strings concatenation and repetition

list11 =[1,2,3,4,5,6,7,7,6,5,1]
list22=['a','b','v','w','x','y','z']
print(list11)
print(list22)
#concatenation
list33 = list11 + list22
print("Concatenating 2 lists \n",list33)
print("Repetiting list 2 times \n",list11*2)
#iterating 
print("\nIterating The List")
for x in list22:
    print (x)
    
#membership 
print(f"is there 3 in list {list11} ? " ,3 in list11)
print(f"is there 3 in list {list11} ? " ,11 in list11)

#finding the length of the list
print(f"length of the list {list11} : \t",len(list11))

#Indexing, slicing 
#Because list all sequences indexing and slicing work the same way for lists as they do for strings

list_pro = ["python", "c","c#","java","JavaScript","Ruby","PHP","Rust","Go"]
print (list_pro)
print(len(list_pro)," -- length ")
print("substring : ",list_pro[2:6])
print("substring2 : ",list_pro[5:8])
print("substring2 : ",list_pro[3:5])

print("list[0]: ",list_pro[0])
print("list[8]: ",list_pro[8])
print("list[7]: ",list_pro[7])
print("list[4]: ",list_pro[4])
print("list[-1]: ",list_pro[-1])
#list methods

list_pro.append('c++')
print("Added C++ to the list using append()")
print(list_pro)
list_pro.pop(6)
print("removed PHP from the list using pop()")
print(list_pro)
# del list_pro
# print(list_pro)
print("Index of Rust : ",list_pro.index("Rust"))
print("Clearing the list : " ,list_pro.clear())
print("\t",list_pro,"\tReturns the empty list")
list111 = list11.copy()
print("Copied a list : ",list111)
print("count 7 : ",list111.count(7))
listt=[1,2,3,4,5,6,7,8,9]
print(listt)
listt.reverse()
print(listt,"Reverse")
unorder_list=[4,6,8,2,9,3,5,7,1,9,0,8,55,22,222,00]
print("unodered list : ",unorder_list)
unorder_list.sort()
print("Ordered list : ",unorder_list)
unorder_list.insert(0,"abc")
print("added abc : ",unorder_list)

#building list functions --length length maximum minimum
_list =[1,0,-1,2,3,6,9,4,2,00,44,99,22,66,37,89531,2223456,8990]
print(_list)
print("length : ",len(_list))
print("maximum : ",max(_list))
print("minimum : ",min(_list))
tuple1=(1,2,3,5,6)
listT=list(tuple1)
print(f"converting tuple {tuple1} to {listT}")
str_a = "Hello world"
list_str = list(str_a)
print(f"converting string {str_a} to {list_str}")




