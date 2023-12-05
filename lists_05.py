numbers = []

for i in range(1, 101):
    numbers.append(i)


for number in numbers:
    print(number, end=' ')

print()

number_of_list_elements = len(numbers)
print(f'Lista "numbers" ima: {number_of_list_elements} elemenata.')
print(f'Lista "numbers" ima: {len(numbers)} elemenata.')