numbers = []
for number in range(21):
    numbers.append(number)

print()
print('Ispis CIJELE LISTE')
for i in numbers:
    print(i, end=' ')
print('\n')

# CTRL + K + C -> komentiranje - Comment
# CTRL + K + U -> dekomentiranje - Uncomment

#region Ostatak koda

# Birsanje svih elemenata liste
# numbers.clear()
# print('Ispis LISTE nakon clear()')
# for i in numbers:
#     print(i, end=' ')
# print('\n')


# Kopiranje svih elemenata liste
# numbers_copy = numbers.copy()
# print('Ispis LISTE nakon copy()')
# for i in numbers:
#     print(i, end=' ')
# print('\n')
# print('Ispis nove LISTE nakon copy()')
# for i in numbers_copy:
#     print(i, end=' ')
# print('\n')

# numbers_copy = numbers
# numbers_copy[10] = 'Python'

# print('Ispis LISTE nakon copy()')
# for i in numbers:
#     print(i, end=' ')
# print('\n')
# print('Ispis nove LISTE nakon copy()')
# for i in numbers_copy:
#     print(i, end=' ')
# print('\n')

#endregion

# Prebrojavanje koliko puta se u listi pojavljuje element
numbers[3] = 15
element = 15
number_count = numbers.count(element)

print(f'Element {element} se pojavljuje u listi {number_count} puta.')






for i in numbers:
    print(i, end=' ')
print('\n')