num1 = int(input())
num2 = int(input())
print("Sum:",num1+num2)
print(f"Sum:{num1+num2}")

#Finding the area of circle
radius = float(input("Enter the radius:"))
print("Area o circle: ",3.14*radius*radius)

#Solving quadratic equation
a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
root1 = 0
root2 = 0
d = b**2 - 4*a*c
root1 = (-b + (d**0.5)) / (2*a)
root2 = (-b - (d**0.5)) / (2*a)
print(f"Roots:({root1}),({root2})")

#Swapping two numbers
a = int(input("Enter a:"))
b = int(input("Enter b:"))
temp = a
a = b
b = temp
print("After swapping: a=",a,"b=",b)
print(f"After swapping: a={a},b={b}",sep="")

##Swapping two numbers withput temp variable
a = int(input("Enter a: "))
b = int(input("ENter b: "))
a = a + b
b = a - b
a = a - b
print("After swapping: a=",a,"b=",b)

