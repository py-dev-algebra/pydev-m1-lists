### SLICING LISTE ###
# Ponekad želimo od jedne liste dobiti drugu, ali s jasno definiranim članovima prve liste.
# Takvu aktivnost nazivamo slice. Postoji i slice() funkcija, ali mi ćemo koristiti jednostavniju metodu
# koja je jako slična slice(), ali jednako učinkovita, a opet lakša za razumjet.
# Ako smo za pristup jednom elementu liste koristili sintaksu naziv_liste[index] (npr. brojevi[3]),
# možemo istu sintaksu koristiti za pristup više elemenata: naziv_liste[start : stop : step]
# npr. brojevi[3 : 15 : 2] - od trećeg elementa (uključujući), do 15-og elementa (NIJE uključen), korak je 2
# ili svaki drugi. Sječate se range() metode?.
# Ako u prethodnom primjeru želimo uključiti i 15-i element, tada možemo pisati "brojevi[3 : 16 : 2]"
# ili "brojevi[3 : (15 + 1) : 2]" - lakše je čitati
# NAPOMENA: Jako je važno zapamtiti da end NIJE uključen u novu listu, nego prvi element prije njega!

# PRIMJER: Imamo listu brojeva od 0 do 100. Želimo iz te liste uzeti svaki šesti broj od broja 20 do 45.
# Prvo pripremimo listu brojeva
brojevi = []
for broj in range(0, 101):
    brojevi.append(broj)

# Kreiramo variajblu u koju ćemo pohraniti novu listu izdvojenih brojeva
# te pomoću slične sintakse za pristup elementu liste lista[0] 
# izdvojimo sve elemente od 20 do 45 + 1 uz korak od 6, jer je svaki 6.
izdvojeni_brojevi = brojevi[20 : (45 + 1) : 6]      # od 20, do 46, svaki 6.
for i in izdvojeni_brojevi:
    print(i, end=' ')

### SLICING SINTAKSA ###
# Sintaksa općenito: NAZIV_LISTE[START : STOP : STEP]
# Iskoristimo gornji primjer i prikažimo i ostale mogućnosti
brojevi = []
for broj in range(0, 101):
    brojevi.append(broj)

izdvojeni_brojevi = brojevi[20 : (45 + 1) : 6]
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')

# NAZIV_LISTE[START : STOP]     # elementi od START do STOP - podrazumijeva se da je STEP = 1
print('NAZIV_LISTE[START : STOP]')
izdvojeni_brojevi = brojevi[20 : 45]      # od 20 do 45 (NIJE uključen)
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')

# NAZIV_LISTE[START :]     # elementi od START do kraja liste koliko god elemenata bilo - podrazumijeva se da je STEP = 1
print('NAZIV_LISTE[START :]')
izdvojeni_brojevi = brojevi[20 :]      # od 20 do 100 (100 JE uključen)
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')

# NAZIV_LISTE[: STOP]     # elementi od prvog elementa liste do STOP - podrazumijeva se da je STEP = 1
print('NAZIV_LISTE[: STOP]')
izdvojeni_brojevi = brojevi[: 45]      # od prvog elementa do 45 (NIJE uključen)
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')

# Cijela lista
# NAZIV_LISTE[ : ]     # elementi od prvog elementa do kraja liste koliko god elemenata bilo - podrazumijeva se da je STEP = 1
print('NAZIV_LISTE[ : ]')
izdvojeni_brojevi = brojevi[ : ]      # od 0 do 100 (100 JE uključen)
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')


# NAZIV_LISTE[START : STOP : STEP]     # elementi od START do STOP uz definiran STEP
print('NAZIV_LISTE[START : STOP : STEP]')
izdvojeni_brojevi = brojevi[20 : 45 : 6]      # od 20 do 45 (NIJE uključen), svaki 6-i element
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')

# Što kada su START, STOP i STEP brojevi s negativnim predznakom?
# Tada je sve isto, samo što je početak brojanja kraj liste ... 
# To znači umjesto da ide od početka prema kraju liste, slice počinje od kraja prema početku - obrnutim redoslijedom

# NAZIV_LISTE[-1]     # ZADNJI element liste
print('NAZIV_LISTE[-1]')
izdvojeni_brojevi = brojevi[-1]      # Zadnji element liste - To više nije lista nego element pa nema FOR petlje
#for i in izdvojeni_brojevi:
#    print(i, end=' ')
print(izdvojeni_brojevi, end=' ')
print('\n\n')


# NAZIV_LISTE[-2]     # PREDZADNJI element liste
print('NAZIV_LISTE[-2]')
izdvojeni_brojevi = brojevi[-2]      # Predzadnji element liste - Više nije lista nego element pa nema FOR petlje
#for i in izdvojeni_brojevi:
#    print(i, end=' ')
print(izdvojeni_brojevi, end=' ')
print('\n\n')


# NAZIV_LISTE[-START : ]     # elementi od PREDZADNJEG ELEMENTA do kraja liste - podrazumijeva se da je STEP = 1
print('NAZIV_LISTE[-START : ]')
izdvojeni_brojevi = brojevi[-2 : ]      # od 99 do 100 (100 JE uključen)
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')

# NAZIV_LISTE[ : -STOP]     # elementi od prvog elementa do PREDZADNJEG - podrazumijeva se da je STEP = 1
print('NAZIV_LISTE[ : -STOP]')
izdvojeni_brojevi = brojevi[ : -2]      # od 0 do 99 (99 NIJE uključen)
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')

# NAZIV_LISTE[ :  : -STEP]     # elementi od početka do kraja uz korak -1
print('NAZIV_LISTE[ : : -STEP]')
izdvojeni_brojevi = brojevi[ : : -1]      # cijela lista, ali obrnutim redoslijedom
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')


# NAZIV_LISTE[START :  : -STEP]     # elementi od START do kraja uz korak -1 (kada je korak -1 to znači da ide od kraja prama početku)
print('NAZIV_LISTE[START : : -STEP]')
izdvojeni_brojevi = brojevi[1 : : -1]       # Prva dva elementa obrnutim redoslijedom
                                            # U ovom slučaju START je 1 dakle od tog elementa počinje i ide 
                                            # obrnutim smjerom zbog koraka -1, a to znači od elementa 1 prema početku.
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')


# NAZIV_LISTE[ : -STOP : -STEP]     # elementi od START do kraja uz korak -1
print('NAZIV_LISTE[ : -STOP : -STEP]')
izdvojeni_brojevi = brojevi[ : -3 : -1]     # Kada START nije naveden i korak je -1 to znači da kreće od kraja prema
                                            # početku sve dok ne dođe do STOP, a to je treći elementa s kraja jer je STOP = -3
                                            # Treći element s kraja NIJE uključen, zato jer STOP nije uključen.
                                            # ZRezulta je zadnja dva elementa obrnutim redoslijedom
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')


# NAZIV_LISTE[-START :  : -STEP]     # elementi od START do kraja uz korak -1
print('NAZIV_LISTE[-START : : -STEP]')
izdvojeni_brojevi = brojevi[-3 : : -1]      # START je -3, a to znači treći elementa od kraja uz korak -1 
                                            # To znači da idemo obrnutim redoslijedom, odnosno prema početku liste
                                            # Rezultat je cijela lista osim zadnja dva elementa. 
                                            # START JE uključen u rezultat pa je zato i treći element s kraja uključen, 
                                            # a preedzadnji i zadnji nisu.
for i in izdvojeni_brojevi:
    print(i, end=' ')
print('\n\n')
