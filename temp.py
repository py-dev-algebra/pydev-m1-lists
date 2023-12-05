contacts = []

for i in range(2): #0,1
    first_name = input(f'Upišite ime {i + 1}. kontakta: ')
    last_name = input(f'Upišite prezime {i + 1}. kontakta: ')
    phone = input(f'Upišite broj telefona {i + 1} kontakta: ')

    contacts.append(first_name)
    contacts.append(last_name)
    contacts.append(phone)

for contact in contacts:
    print(contact, end= ' ') 