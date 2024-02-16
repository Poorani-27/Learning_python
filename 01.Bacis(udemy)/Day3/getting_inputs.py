# Get an integer input
age = int(input("Enter your age: "))

# Get a float input
height = float(input("Enter your height in meters: "))

# Get a string input
name = input("Enter your name: ")

# Get multiple inputs in a single line and unpack them
num1, num2 = map(float, input("Enter two numbers separated by space: ").split())

# Display the results
print("\nResults:")
print("Age:", age)
print("Height:", height, "meters")
print("Name:", name)
print("num1 = ", num1)
print("num2 = ", num2)


