a=(1,2.5,"RUN",True)
print(a)
print(type(a))
#####indexing
print(a[1])
print(a[-1])
### converting
b=list(a)
print(b)
b.append("Kavi")
print(type(b))
b=tuple(b)
print(b)
print(type(b))
a=list(a)
b=list(b)
a.extend(b)
a=tuple(a)
print(a)
###len
print(len(a))
###for loop
for i in a :
    print(i)

#single value in tuple doesn't consider as tuple
c=(1)
print(c)
print(type(c))
c=(1,)
print(c)
print(type(c))

#concatenate
print(a)
b=tuple(b)
print(b)
c=a+b
print(c)
##count
print(c.count("Kavi"))
########################################## nested tuples #########################
a=[1,2,3,4,8,9,9,9]
b=['p','o','o','r','a','n','i']
c=(a,b)
print(c)
print(c[0][4])
print(type(a))
