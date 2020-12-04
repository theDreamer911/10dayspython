import re

nomor_hp = "081-225-900-513"

if re.search("\w{3}-\w{3}-\w{3}-\w{3}", nomor_hp):
    print('Ini nomor hp yang benar')
else:
    print('Nomor tidak sesuai')


# if we checked number we can use \w or \d
