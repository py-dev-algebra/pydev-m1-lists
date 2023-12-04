first_name = 'Pero'
last_name = 'Peric'
year_of_birth = 1998

message = f'Ime i prezime: {first_name} {last_name} - {year_of_birth}'
# 'Ime i prezime: Pero Peric - 1998'

# print(message)
for letter in message:
    print(letter, end='-')
