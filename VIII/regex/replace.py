import re

# food = "hat rat mat pat gat nat lat zat xat"

# replace = re.compile("[r]at")

# food = replace.sub("food", food)

# print(food)


randstr = "Here is \\orange"

print(re.search(r"\\orange", randstr))
