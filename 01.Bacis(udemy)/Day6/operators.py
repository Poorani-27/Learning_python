#Arithmetic operators

# Addition
result_addition = 5 + 3
print("Addition:", result_addition)

# Subtraction
result_subtraction = 8 - 2
print("Subtraction:", result_subtraction)

# Multiplication
result_multiplication = 4 * 6
print("Multiplication:", result_multiplication)

# Division
result_division = 10 / 2
print("Division:", result_division)

# Floor Division
result_floor_division = 10 // 3
print("Floor Division:", result_floor_division)

# Modulus
result_modulus = 10 % 3
print("Modulus:", result_modulus)

# Exponentiation
result_exponentiation = 2 ** 3
print("Exponentiation:", result_exponentiation)

#Relational Operators

# Equal to
result_equal = (5 == 5)
print("Equal to:", result_equal)

# Not equal to
result_not_equal = (5 != 3)
print("Not equal to:", result_not_equal)

# Greater than
result_greater_than = (8 > 5)
print("Greater than:", result_greater_than)

# Less than
result_less_than = (3 < 5)
print("Less than:", result_less_than)

# Greater than or equal to
result_greater_than_equal = (5 >= 5)
print("Greater than or equal to:", result_greater_than_equal)

# Less than or equal to
result_less_than_equal = (3 <= 5)
print("Less than or equal to:", result_less_than_equal)

#Logical Operators 
# AND
result_and = (True and False)
print("AND:", result_and)

# OR
result_or = (True or False)
print("OR:", result_or)

# NOT
result_not = not True
print("NOT:", result_not)

#Bitwise Operators
# Bitwise AND
result_bitwise_and = 0b1100 & 0b1010
print("Bitwise AND:", bin(result_bitwise_and))

# Bitwise OR
result_bitwise_or = 0b1100 | 0b1010
print("Bitwise OR:", bin(result_bitwise_or))

# Bitwise XOR
result_bitwise_xor = 0b1100 ^ 0b1010
print("Bitwise XOR:", bin(result_bitwise_xor))

# Bitwise NOT
result_bitwise_not = ~0b1100
print("Bitwise NOT:", bin(result_bitwise_not))

# Left Shift
result_left_shift = 0b1100 << 2
print("Left Shift:", bin(result_left_shift))

# Right Shift
result_right_shift = 0b1100 >> 1
print("Right Shift:", bin(result_right_shift))

#assignment
# Shorthand Assignment
x = 5
x += 3
print("Shorthand Addition:", x)

y = 8
y /= 2
print("Shorthand Division:", y)


# Identity Operators
a = [1, 2, 3]
b = [1, 2, 3]

result_is = (a is b)
result_is_not = (a is not b)

print("Identity (is):", result_is)
print("Identity (is not):", result_is_not)

# Membership Operators
list_example = [1, 2, 3, 4, 5]

result_in = (3 in list_example)
result_not_in = (6 not in list_example)

print("Membership (in):", result_in)
print("Membership (not in):", result_not_in)
