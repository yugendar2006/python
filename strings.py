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
