try:
    age = int(input('Age: '))
    if age > 1:
        print(f"You are {age} years old")
    elif age == 1 or age == 0:
        print(f"You are {age} year old")
    else:
        print(f"You input {age}, age invalid")
except ValueError:
    print('You put an invalid age')
print('Execution continues')
