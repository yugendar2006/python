# input statements
name = input()
print("My name is", name)

number = input("Enter a number: ")
print(type(number))
a = int(number)
print(type(a))
number = int(input("Enter a number:"))
print(type(number))
b = float(number)
print(type(b))

name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello!", name, "your age is", age)

#Seperator
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print(a,b)
print(a,b,sep="-")
print(a,b,end="Ended here")

name = input()
print("Hello", name,sep=",",end="!")

number = int(input("Enter a number: "))
print("You entered:", number,sep="")

value = float(input("Enter a float value: "))
print("value of pi:",value,sep="")

numbers = list(map(int, input("Enter three numbers: ").split()))
print(numbers)
print("sum of three numbers: ",sum(numbers))
#input() → "10 20 30"
#.split() → ["10", "20", "30"]
#map(int, ...) → converts each to integer
#list() → [10, 20, 30]
#another way
a = input()
x,y,z = a.split()
print(x,y,z)
sum = int(x) + int(y) + int(z)
print(sum)

n = int(input("Enter n: "))
print("5 4 3 2 1",end=" Blast off!")
