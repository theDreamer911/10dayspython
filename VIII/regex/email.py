import re

email = "jhn@lan.com get @.com @ceo.start.com start@up.com"

print("EmailMatches:", len(re.findall(
    "[\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}", email)))
