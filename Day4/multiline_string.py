multi_line_string = '''
This is a multi-line
string in Python.
It can span multiple lines
without the need for escape characters.
'''

print(multi_line_string)

another_multi_line_string = """
This is another multi-line
string using double triple-quotes.
It provides the same functionality as triple-quotes.
"""

print(another_multi_line_string)

# Triple quotes are more commonly used than single quotes, but they have their uses too.

#getting Multiline String Input From the User

print("Enter your multi-line input. Type 'end' on a new line to finish.")

lines = []
while True:
    line = input()
    if line.lower() == 'end':
        break
    lines.append(line)

multi_line_input = '\n'.join(lines)

print("Your multi-line input:")
print(multi_line_input)
 
