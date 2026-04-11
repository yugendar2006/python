num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))
operator = input("Give opertor:")

if opertor == "+":
    print("The sum is: ", num1+num2)
elif opertor == "-":
    print("The difference is: ", num1-num2)
elif opertor == "*":
    print("The product is: ", num1*num2)
elif operor == "/":
    if num2 != 0:
        print("The quotient is: ", num1/num2)
    else:
        print("Error: Divsion by zero is not allowed.")
