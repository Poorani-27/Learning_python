string="Hello world, following are examples for string method"
print("string:",string,"\n")
print('lower: ',string.lower(),"\n")
print('upper: ',string.upper(),"\n")

print('capitalize: ',string.capitalize(),"\n")

print('title: ',string.title(),"\n")
print("swapcase :",string.swapcase(),"\n")

print('casefold: ',string.casefold(),"\n")

print('center: ', string.center(104, '*'), "\n")

print('count:\'a\' is present ',string.count('a')," times","\n")

print('encode: ',string.encode('ibm039'))
print('encode: ',string.encode('utf-16'),"\n")

print('endswith "ed": ',string.endswith('ed'))
print('endswith "od": ',string.endswith('od'),"\n")

string1='\thello\t||world'
print('expandtab: ',string1.expandtabs(66),"\n")

print('find "a": ',string.find('a'),"\n")


string11="Hello '{}', following are examples for '{}' method"
print(string11)
string1="Hello{}, following are examples for {} method"
print("format:",end="")
print(string1.format(' world',' string'),end='\n')


a = "{'x':'good', 'y':'morning'}"
print('\n',a)
a = {'x':'good', 'y':'morning'}
print("{x}'s last name is {y}".format_map(a),end="\n")


print("index  of a :",string.index('a'),end="\n")

print("isalnum :",string.isalnum(),end="\n")


print("isalpha :",string.isalpha(),"returns false because it contains space")
print("\n") 


print('ljust: ',string.ljust(300),"\n")

print('lstrip: ',string.lstrip(),"\n")

print('partition: ',string.partition("are"),"\n")

print('replace:',string.replace('Hello','Hi'),"\n")

print('rfind:',string.rfind("are"),"\n")

print('rpartition:',string.rpartition("for"),"\n")

print('rsplit:',string.rsplit('*'),"\n")

print('rjust:',string.rjust(30),"\n")

print('rstrip:',string.rstrip(),"\n")


print('ljust: ',string.ljust(300),"\n")

strr="cat\fdog\fmonkey\fdonkey"
print("splitness:",strr.splitlines(),end="\n")

string12="           Hello world, following are examples for string method               "
print('strip:',string12.strip(" "),"\n")

print('zfill:',string.zfill(100),"\n")
