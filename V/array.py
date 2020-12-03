# # from array import array

# # numbers = array("i", [1, 2, 3])
# # numbers.append(2)
# # # numbers.insert(0) --> this is wrong
# # # numbers.pop(4)
# # numbers[0] = 3
# # print(numbers)


# numbers = [1, 1, 1, 2, 3, 4]
# first = set(numbers)
# second = {1, 4, 7, 8}
# # second.add(5)
# # second.remove(5)

# print(first | second)
# print(first & second)
# print(first - second)
# print(second - first)
# print(first ^ second)


# if 1 in first:
#     print('yes')

# Defininf dictionary
# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# point["x"] = 10
# point["z"] = 20
# if "a" in point:
#     print(point["a"])
# print(point.get("a", "not exist"))
# del point['x']
# print(point)

# # for key in point:
# #     print(key, point[key])

# for key in point.items():
#     print(key)

# for key, value in point.items():
#     print(key, value)


# values = []
# for x in range(5):
#     values.append(x *2)

# {1,2,3,4} # set
# {1:"a", 2: 'b'} # dictionary

# values = {x: x*2 for x in range(5)}
# print(values)

# [expression for item in items]

# values = {}
# for x in range(5):
#     values[x] = x * 2

values = (x*2 for x in range(5))
print(values)
