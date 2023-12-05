# Napisite program koji zbraja brojeve od 1 do nekog broja.
# Ispiste zboj te ispiste srednju vrijednost (zbroj / broj elemenata)


# od 1 do 35
numbers = []

sum_limit = int(input('Upisite broj do kojeg zelite zbrajati: '))


numbers_sum = 0

for i in range(1, sum_limit + 1):
    #numbers_sum = numbers_sum + i
    numbers_sum += i
    numbers.append(i)

print(f'Zbroj brojeva od 1 do {sum_limit} je: {numbers_sum}')
print(f'Prosjek brojeva od 1 do {sum_limit} je: {numbers_sum / len(numbers)}')
