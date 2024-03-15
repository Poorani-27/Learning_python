a={"a",5,"poorani","kavi",4.5,True}
print(type(a))
print(a)

## no duplicate
a.add('b')
print(a) #UNORDERED 
a.add(True)
print(a)
c={1,2,1,2,3,4,2,1,32,1,1,1,1,2,2,3,3,31,1}
print("c={1,2,1,2,3,4,2,1,32,1,1,1,1,2,2,3,3,31,1} ")
print(c)
a={1,2,3,4,5}
b={4,5,6,7,8,9}
print( a, "\n",b )
c=a.union(b)
d=a.intersection(b)
print("union: ",c)
print("intersection: ",d)
e=a.difference(b)
print("difference ",e)
####################### update
print(a)
print(b)
a.update(b)
print(a)

###############  remove and discard

a.remove(9)
print(a)

try :
    a.remove(11) ###### throws error
    print(a)
except:
    print("out of index")

a.discard(13)
print(a)

a={1,2,3,4,5}
b={4,5,6,7,8,9}
### built 
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)


a={1,2,3,4,5}
b={1,2,3}
### built 
c=a.isdisjoint(b)
print(c)
c=a.issubset(b)
print(c)
c=a.issuperset(b)
print(c)
c=b.issubset(a)
print(c)
