# def greet(first_name, last_name):
#     print(f'Hi {first_name} {last_name}')
#     print('Welcome Aboard')


# greet("Alex", "Hand")
# greet("Hand", "Snow")

# def greet(name):
#     # print(f'Hi {name}')
#     return "..."


# print(greet('hand'))

# def get_greeting(name):
#     return f"Hi {name}"


# message = get_greeting("Hand")
# file = open("content.txt", 'w')
# file.write(message)


# def increment(number, by):
#     return number+by


# # result = increment(2, 1)
# # print(result)

# print(increment(2, 1))
# print(increment(2, by=2))
# print(increment(number=10, by=2))

# def increment(number, by=1):
#     return number + by


# print(increment(2, 5))


# def multiply(*numbers):
#     # print(numbers)
#     total = 1
#     for number in numbers:
#         # print(number)
#         # total = total * number
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# def save_user(**user):
#     print(user["id"])


# save_user(id=1, name="Hand", age=18)

# message = "a"


# def greet(name):
#     global message
#     message = "b"


# greet("John")
# print(message)


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print('start')
print(multiply(1, 2, 3))
print(multiply(1, 2, 3))
print(multiply(1, 2, 3))
