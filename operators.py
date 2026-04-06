a = 5
b = 2
# Arithmetic operators
print("Addition:",a+b)
print("subtraction:",a-b)
print("Multiplication:",a*b)
print("Division:",a/b)#prints a float value
print("Floor Division:",a//b)#prints an integer value
print("Modulus:",a%b)#prints the remainder of the division
print("Exponentiation:",a**b)

#Assignment operators
a = 6
b = 3
b = a
print(a)
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)

#comparison operators
a = 5
b = 3
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)
print(a > b)
print(a < b)

#Logical operators
a = True
b = False
print(a and b)
print(a or b)
print(not a)

#membership operators
a = ["20","30","40"]
print("20" in a)
print("80" not in a)

#identity operators
a = 5
b = 3
c = a
print(a is c)
print(a is not b)

#Bitwise operators
a = 3
b = 2
print(a & b)#AND
print(a | b)#OR
print(a ^ b)#XOR
print(~a)#NOT
print(a << 2)
print(a >> 2)

#precedence of operators
a = 5 + 3 * 2
print(a)
