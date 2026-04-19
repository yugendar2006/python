s = "HelloWorld"
print(s[0])
print(s[::2])
print(s[1::2])
print(s[::-1])

#string concatenation
first_name = "yugendar"
last_name = "Chowdary"
print("My name is: ",first_name+last_name)

#string length
s="yugendar"
print("length of s=",len(s))
s="Hello World!"
print(len(s))

s = "Hello World!"
print(s.upper())#convert string to uppercase
print(s.lower())#convert string to lowercase
print(s.strip())#remove leading and trailing whitespace
print(s.replace("World","python"))#replace susbstring

s = "hello"
print(s * 3)
print(s ** 3)

s = input()
a = s.count("a")
e = s.count("e")
i = s.count("i")
o = s.count("o")
u = s.count("u")
print("Number of vowels= ",sum([a,e,i,o,u]))
print(f"Number of vowels is: {a+e+i+o+u}")

#grade calculator
m = int(input("Enter marks: "))
s = int(input("Enter marks: "))
e = int(input("Enter marks: "))
total_marks = m + s + e
average = total_marks/3

percentage = (total_marks/300)*100
grade = ""
if percentage >= 90:
    grade = "A" 
elif percentage >= 80 and percentage <= 90:
    grade = "B"
elif percentage >= 70 and percentage <= 80:
    grade = "C"
else:
    grade = "D"
