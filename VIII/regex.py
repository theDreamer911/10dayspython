import re

TraceStudent = '''
Agung is 175cm and Adenta is 171cm
Aljevon is 172cm and Agra is 165cm
'''

tall = re.findall(r'\d{1,3}', TraceStudent)         # d{1,3} mengambil 3 angka
names = re.findall(r'[A-Z][a-z]*', TraceStudent)
# [A-Z][a-z] mengambil karakter yang mengandung huruf besar dan kecil

tallDict = {}

x = 0

for eachname in names:

    tallDict[eachname] = tall[x]
    x += 1

print(tallDict)
