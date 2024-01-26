import math
print("Sin Value of 3 : ",math.sin(3))
print("Sin value of -3 : ",math.sin(-3))
print("Sin value 0f pi : ",math.sin(math.pi))

print("cos Value of 3 : ",math.cos(3))
print("cos value of -3 : ",math.cos(-3))
print("cos value 0f pi : ",math.cos(math.pi))

print("tan Value of 3 : ",math.tan(3))
print("tan value of -3 : ",math.tan(-3))
print("tan value 0f pi : ",math.tan(math.pi))

#Inverse 

print("asin Value of 3 : ",math.asin(0.3))
print("asin value of -3 : ",math.asin(-0.3))

print("cos Value of 3 : ",math.acos(0.3))
print("cos value of -3 : ",math.acos(-0.3))

print("atan Value of 3 : ",math.atan(0.3))
print("atan value of -3 : ",math.atan(-0.3))

#trigonometric misc function

#hypo (X,Y)
#degrees(x) converts angle from radian to degree
#radians(x) converts angle from degree to radian

print ("The Degree of pi : " , math.degrees(math.pi))
print ("The radian of 180deg : " , math.radians(180))

import math

# Hyperbolic sine (sinh)
x = 2
sinh_result = math.sinh(x)
print("Hyperbolic Sine of", x, "is:", sinh_result)

# Hyperbolic cosine (cosh)
cosh_result = math.cosh(x)
print("Hyperbolic Cosine of", x, "is:", cosh_result)

# Hyperbolic tangent (tanh)
tanh_result = math.tanh(x)
print("Hyperbolic Tangent of", x, "is:", tanh_result)

def hypo(x, y):
    return math.sqrt(x**2 + y**2)

# Example usage
side_a = 3
side_b = 4

hypotenuse = hypo(side_a, side_b)
print(f"The hypotenuse of the right-angled triangle with sides {side_a} and {side_b} is: {hypotenuse}")

