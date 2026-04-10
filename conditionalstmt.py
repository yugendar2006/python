age = int(input("Enter youre age" ))
if (age >= 18):
    print("You are eligible to vote")

#if-else
age = 100
if age <= 12:
    print("Travel for free.")
else:
    print("Pay for ticket.")

#elif
age = 2
if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

#Nested if
age = 20
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")
