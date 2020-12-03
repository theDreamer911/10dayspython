# def fizz_buzz(number):

#     if number % 15 == 0:
#         return 'fizzbuzz'
#     if number % 3 == 0:
#         return 'fizz'
#     if number % 5 == 0:
#         return 'buzz'
#     else:
#         return number


# print(fizz_buzz(5))

def fizz_buzz():
    number = int(input('Angka:'))

    if (number % 3 == 0) and (number % 5 == 0):
        print('fizzBuzz')
    elif number % 3 == 0:
        print('fizz')
    elif number % 5 == 0:
        print('buzz')
    else:
        print(number)


fizz_buzz()
