import re

# randstr = "12345"

# print("Matches:", len(re.findall("\d{5}", randstr)))


num = "123 11234 21414 3512 123456 1234567"

print("Matches:", len(re.findall("\d{5,7}", num)))
