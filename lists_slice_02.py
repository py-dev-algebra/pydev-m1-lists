numbers = []

for number in range(100, 201):
    numbers.append(number)

#                           S    F   Step
# selected_numbers = numbers[20 : 45 : 10] # -> od indeksa 20 do indeksa 45 dvaki deseti
# print(selected_numbers)

# Sve elemente od prvog do 45-og
# selected_numbers = numbers[0 : 45 : 2]
# selected_numbers = numbers[ : 45 : 2]
# print(selected_numbers)


# selected_numbers = numbers[45 : 0 : -2]
# print(selected_numbers)

# last_element = numbers[-1]
# before_last_element = numbers[-2]

# selected_numbers = numbers[-1 : : -1]
# print(selected_numbers)

# selected_numbers = numbers[ : : -1]
# print(selected_numbers)

text = 'Programiranje'
obrnuto = text[ : : -1]
print(obrnuto)
