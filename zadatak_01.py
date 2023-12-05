# upisite u listu onoliko kontakta koliko korisnik to zeli. 
# Svaki kontakt ima: ime, prezime, broj telefona.
# Omogucite korisniku unos vrijednosti kontakta

contacts = []

number_of_contacts = int(input('Upisite koliko kontakta zelite dodati? '))


for i in range(number_of_contacts):
    first_name = input(f'Upisite ime {i + 1}. kontakta: ')
    last_name = input(f'Upisite prezime {i + 1}. kontakta: ')
    phone = input(f'Upisite broj telefona {i + 1}. kontakta: ')

    contacts.append(first_name)
    contacts.append(last_name)
    contacts.append(phone)


list_index_counter = 0
for i in range(number_of_contacts):
    print(contacts[list_index_counter], end=' ')
    print(contacts[list_index_counter + 1], end=', ')
    print(contacts[list_index_counter + 2])

    list_index_counter = list_index_counter + 3
