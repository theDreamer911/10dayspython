import re

str = "Sat, mat, hat, pat"
gold = str.lower()

allstr = re.findall('[m-z]at', gold)  # inside
allstr = re.findall('[^m-z]at', gold)  # outside

for i in allstr:
    print(i)
