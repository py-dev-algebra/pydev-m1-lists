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


# Prebrojavanje koliko puta se u listi pojavljuje element
# numbers[3] = 15
# element = 15
# number_count = numbers.count(element)

# print(f'Element {element} se pojavljuje u listi {number_count} puta.')


# element = 10
# index_of_element = numbers.index(element)
# print(f'Element {element} se u listi nalazi na indeksu {index_of_element}.')


# text = 'Programiranjea'
# index_of_letter = text.index('a')
# print(f'Slovo "a" se u rijeci {text} nalazi na poziciji {index_of_letter + 1}.')
# index_of_letter = text.index('a', index_of_letter + 1)
# print(f'Slovo "a" se u rijeci {text} nalazi na poziciji {index_of_letter + 1}.')
# index_of_letter = text.index('a', index_of_letter + 1)
# print(f'Slovo "a" se u rijeci {text} nalazi na poziciji {index_of_letter + 1}.')

# index_of_letter = 0
# for letter in text:
#     index_of_letter = text.index('a', index_of_letter + 1)
#     print(f'Slovo "a" se u rijeci {text} nalazi na poziciji {index_of_letter + 1}.')

#endregion

# Ispis sortirane liste
# Sortiranje liste od manjeg prema vecem
# numbers.sort()
# for i in numbers:
#     print(i, end=' ')
# print('\n')


# Sortiranje liste od veceg prema manjem
#numbers.sort(reverse=True)
numbers.reverse()
for i in numbers:
    print(i, end=' ')
print('\n')


# print('Ispis pomocu reverseD()')
# for i in reversed(numbers):
#     print(i, end=' ')
# print('\n')

print('Ispis pomocu sorteD()')
for i in sorted(numbers):
    print(i, end=' ')
print('\n')


for i in numbers:
    print(i, end=' ')
print('\n')