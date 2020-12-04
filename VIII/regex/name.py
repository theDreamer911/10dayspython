import re

if re.search("\w{2,20}\s\w{2,20}", "Handhika Yanuar"):
    print("Fullname is valid")
else:
    print('Fullname invalid')
