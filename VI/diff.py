# try:
#     age = int(input('Age: '))
#     xfactor = 10 / age
# except ValueError:
#     print("You didn't enter a valid age")
# except ZeroDivisionError:
#     print("You didn't enter a valid age")
#     # print('Age can\'t be zero')
# else:
#     print("No exceptions were thrown")

try:
    age = int(input('Age: '))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("No exceptions were thrown")
