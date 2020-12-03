# # temperature = 19
# # if temperature > 30:
# #     print('it\'s warm')
# #     print("Drink water")
# # elif temperature > 20:
# #     print('it\'s cloudy')
# # else:
# #     print('it\'s cold')
# # print("Done")


# # trenary
# # age = 22
# # if age >= 18:
# #     print("Eligible")
# # else:
# #     print("Not eligible")

# # age = 22
# # if age >= 18:
# #     message = "Eligible"
# # else:
# #     message = "Not eligible"

# # age = 22
# # message = "Eligible" if age >= 18 else "Not eligible"
# # print(message)


# # logical operator
# high_income = False
# good_credit = True

# if high_income and good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# if high_income or good_credit:
#     print("Eligible")
# else:
#     print("Not Eligible")

# gamer = False

# if not gamer:
#     print('lie')
# else:
#     print('nahh')


# if(high_income or good_credit) and not gamer:
#     print('bah')
# else:
#     print('gg')


# if 10 == '10':
#     print('a')
# elif "bag" > "apple" and "bag" > "cat":  # True & False = False
#     print("b")
# else:
#     print('c')

# for number in range(5):
#     print('sending a message', number+1, (number + 1) * ".")


# first pyramid

# for number in range(1, 10, 2):
#     print('sending a message', number, (number) * ".")
# print('transfer message 10', "." * 10)
# for num in range(9, 0, -2):
#     print("receive a message", num, (num)*'.')

# successful = True
# for number in range(1, 4):
#     print('Attempt')
#     if successful:
#         print('Successful in', number, 'attempt')
#         break
# else:
#     print('You have tried', number, 'and did\'nt work')


# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")


# print(type(range(5)))

# for x in 'Booya':
#     print(x)

# for x in [1, 2, 3, 4, 5]:
#     print(x)

# number = 100
# while number > 0:
#     print(number)
#     number //= 2
#     number += 1  # will make crash


# command = ""
# # while command != "quit" and command != "QUIT":
# while command.lower() != "quit":
#     command = input(">")
#     print("Echo", command)


# while True:
#     command = input('>')
#     print('ECHO', command)
#     if command.lower() == "quit":
#         break

# my solution
count = 0
for i in range(1, 10):
    if i % 2 == 1:
        pass
    else:
        count += 1
        print(i)

print('we have', count, 'even number')

# mosh
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        print(number)
        count += 1
print('we have', count, 'even number')