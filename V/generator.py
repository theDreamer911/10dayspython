# old list

# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)


# generator
from sys import getsizeof


# values = (x * 2 for x in range(100000))
# # print(values)
# # print("genSize:", getsizeof(values))
# values = [x * 2 for x in range(100000)]
# print("listSize:", getsizeof(values))
# # print(len(values))
# for x in values:
#     print(x)


# unpack

# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers)
# print(1, 2, 3)

# first = [1, 2]
# second = [3]
# values = [*first, 'abc', *second, *'hello']
# # values = list(range(5))
# # values = [*range(5), *"Hello"]
# print(values)


# first = {"x": 1}
# second = {'x': 10, 'y': 2}
# combined = {**first, **second, 'z': 0}
# print(combined)


sentence = "This is a common interview question"
