# Python Learning - Day 2 Progress

## Today's Focus: Compilers, Interpreters, Variables

### 1. Compilers and Interpreters:

#### 1.1 Compiler:
A compiler is a program that translates the entire source code of a program into machine code before execution. This machine code is then executed independently of the original source code.

#### 1.2 Interpreter:
An interpreter translates and executes the source code line by line, interpreting and executing each instruction in real-time.

#### 1.3 Python as an Interpreter Language:
Python is often called an interpreter language because Python code is executed line by line by the Python interpreter. This allows for easy debugging and a more interactive development experience.

#### 1.4 Difference between Compiler and Interpreter:
- **Compiler:** Translates the entire source code before execution. Produces an executable file.
- **Interpreter:** Translates and executes the source code line by line. No separate executable file is generated.

## Variables in Python:

In Python, variables are used to store and manage data. They serve as named containers for values, making it easier to work with information in your programs.

### Declaring Variables:

You can declare a variable and assign a value to it using the following syntax:

variable_name = value

a = 10
b="Hello"

### Rules for  Naming Variables:

1.Must Start with a Letter or Underscore:
Variable names must begin with a letter (a-z, A-Z) or an underscore '_'. 
<br>

2.Consist of Letters, Numbers, and Underscores:
After the initial letter, the variable name can contain letters, numbers, and underscores.
<br>
3.Case-Sensitive:
Python is case-sensitive, meaning message and Message are considered different variables.
<br>
4.Avoid Python Keywords:
Variables cannot have the same name as Python keywords (reserved words).

### Datatypes in Python 

int: Integer values (e.g., x = 42). <br>
float: Floating-point values (e.g., pi = 3.14). <br>
str: Strings (e.g., message = "Hello").<br>
bool: Boolean values (True or False).<br>

### Reassigning Variables

Once you've assigned a value to a variable, you can change its value by reassign

message = "Hello"
message = "Hi"

After this, message will have the value "Hi".

### printing the variables

You can display the value of a variable using the print() function:
name = "John"
print("Hello, " + name + "!")

### Concatenating The Variables

You can concatenate (combine) variables of the same type using the + operator:

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

Here, full_name will be "John Doe".

### Local and Global Variables

In Python, there are two types of variables - local and global.
 
Variables can be local (limited to a specific function or block of code) or global (accessible throughout the entire program).

### id() function 

The id() function returns the identity (memory address) of an object. For example:

x = 42
print(id(x))

This will output a unique identifier for the object x.

### type() function

message = "Hello"
print(type(message))

This will output <class 'str'> indicating that message is of type string.
![Image](https://github.com/Poorani-27/Learning_python/blob/main/Day2/image.png)
