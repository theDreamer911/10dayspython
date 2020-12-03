age = int(input('Age: '))

a_range = range(18, 40, 2)
numbers = list(a_range)

if age in numbers:
    print(f"Your age is {age}, you're allowed here")
else:
    print(f"Your age is {age}, you're not allowed here")
