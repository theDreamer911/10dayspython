
age = int(input('Age: '))

numbers = [*range(18, 40, 2)]

if age in numbers:
    print(f"Your age is {age}, you're allowed here")
else:
    print(f"Your age is {age}, you're not allowed here")
