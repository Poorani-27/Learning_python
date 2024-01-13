# Python Learning - Day 4 Progress

## Today's Focus: Multiline Strings, Input Handling, and Comments

### Tasks Accomplished:

1. **Multiline Strings:**
   - Learned about multiline strings in Python.
   - Created multiline strings using triple-quotes.
   - Explored the benefits of multiline strings for better code readability.

2. **Multiline Input Handling:**
   - Implemented code to receive multiline input from the user.
   - Used a while loop to continuously take input until the user types 'end'.
   - Demonstrated how to concatenate input lines into a single multiline string.

3. **Comments in Python:**
   - Explored the importance of comments in code for documentation and readability.
   - Learned to use single-line comments with `#` and multiline comments using triple-quotes. 
### comments
comments are used to annotate and document code. They are not executed by the Python interpreter and are purely for the benefit of developers to provide explanations, clarify code, or add any relevant information. Comments are ignored during the execution of the program.
<br>
There are two types of comments in Python: single-line comments and multi-line comments. <br>
Single-line comments start with the hash (`#`) symbol and continue until the end of the line.<br>

While Python doesn't have a specific syntax for multi-line comments, you can use triple-quotes (`'''` or `"""`) to create multi-line strings as a workaround. Although these strings are not technically comments, they serve the purpose of documenting code across multiple lines:
<br> 
### When to Use Comments:

1. **Code Explanation:** Use comments to explain complex algorithms or logic to make the code more understandable for others (or even for yourself in the future).

```python
# Calculate the sum of elements in a list
numbers = [1, 2, 3, 4, 5]
sum_result = sum(numbers)  # Using the sum() function
print("Sum:", sum_result)
```

2. **TODO Comments:** Indicate areas in the code that need further attention or implementation.

```python
# TODO: Implement error handling here
def some_function():
    # Code to be implemented
    pass
```

3. **Documentation:** Comments can be used to document functions, classes, and modules. This is often done using docstrings, which are triple-quoted strings placed immediately after the function, class, or module definition.

```python
def add_numbers(a, b):
    """
    This function adds two numbers and returns the result.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    "" return a + b
```

 comments in Python are essential for maintaining clean, readable, and understandable code. They play a crucial role in code documentation, making it easier for developers to collaborate and maintain the codebase.
<br>

 ![Image](https://github.com/Poorani-27/Learning_python/blob/main/Day4/Day4.png)
