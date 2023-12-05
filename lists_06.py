tasks = [
    'Odabrati naziv liste',
    'Unijeti element liste',
    'Pokrenuti aktivnost nad listom ili elementom liste'
]

index = 0
for task in (tasks):
    print(f'{index + 1}. zadatak: {task}')
    index += 1
print()


tasks.append('Ispisati sve elemente liste')
index = 0
for task in (tasks):
    print(f'{index + 1}. zadatak: {task}')
    index += 1
print()


tasks[1] = 'Napisati naziv liste koju zelimo promijeniti'
index = 0
for task in (tasks):
    print(f'{index + 1}. zadatak: {task}')
    index += 1
print()
