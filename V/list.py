# letters = ["a", 'b', 'c', 'd']
# matrix = [[0, 1], [2, 3]]
# zeros = [0]*5
# combined = zeros+letters
# number = list(range(20))
# char = list('hello World')

# # print(len(char))
# char[4] = ''
# # print(char[1])
# # print(char)
# letters[0] = 'A'
# print(letters[0:3])
# print(letters[:])
# print(letters[::2])

# numbers = list(range(20))
# print(numbers[::2])
# print(numbers[::-2])


# numbers = [1, 2, 3, 4, 5, 4, 5, 5, 5]
# first, second, *other = numbers
# print(first)
# print(other)


# letters = ['a', 'b', 'c']
# items = (0, 'a')
# index, letter = items

# letters = ['a', 'b', 'c']
# for index, letter in enumerate(letters):
#     # print(letter)
#     # print(leprtter[0], letter[1])
#     print(index, letter)


# letters = ['z', 'x', 'y', 'a', 'b', 'c', 'k', 'k', 'k']

# letters.append('e')
# letters.insert(2, 'dd')
# print(letters)

# letters.pop(2)
# letters.remove('e')
# letters.append('f')
# letters.append('g')
# del letters[0:2]
# print(letters)

# if 'k' in letters:
#     print(letters.index('k'))
#     print(letters.count('k'))

# letters = ['z', 'x', 'y', 'a', 'b', 'c', 'k', 'k', 'k']

# letters.sort(reverse=True)
# print(sorted(letters, reverse=True))
# print(letters)


# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
#     ("Product3", 4),
#     ("Product3", 20),
# ]


# def sorting_item(item):
#     return item[1]


# items.sort(key=sorting_item)
# print(items)

# items.sort(key=lambda item: item[1])
# print(items)


# map function

# prices = []
# for item in items:
#     prices.append(item[1])

# price = list(map(lambda item: item[1], items))
# print(price)
# for item in price:
#     print(item)


items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
    ("Product3", 4),
    ("Product3", 20),
]

# filtered = list(filter(lambda item: item[1] >= 10, items))
# print(filtered)


price = list(map(lambda item: item[1], items))

prices = [item[1] for item in items]
print(prices)

filtered = list(filter(lambda item: item[1] >= 10, items))
filtering = [item for item in items if item[1] >= 10]
print(filtering)
