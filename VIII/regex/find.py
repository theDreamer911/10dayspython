import re

# searching information

# if re.search('inform', 'we need to inform him with the latest information'):
#     print('This is inform')


allinform = re.findall(
    'inform', 'we need to inform him with the latest information')

for i in allinform:
    print(i)  # it will print two inform, because information has inform too


def text():
    stringg = 'we need to inform him with the latest information'
    # print(str)


# find()
