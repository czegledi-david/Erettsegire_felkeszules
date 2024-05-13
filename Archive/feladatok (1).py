# 1. feladat
"""
for i in range(1, 21):
    print(i)
print()
# 2. feladat
"""
for i in range(-90, 90, 20):  #110
    print(i)
print()
# 3. feladat
import random

x = 2

for i in range(1, 11):
    print(i * x)
    #print(str(i) + "*" + str(x) + " = " + str(i * x))

"""
# 4. feladat
for i in range(8:00, 12:00):
    print(i)
"""
"""
for i in range(8, 13):
    for j in range(0, 60, 20):
        if (i == 12):
            print(str(i) + ":" + str(j) + "0")
            break
        if (j <= 0):
            print(str(i) + ":" + str(j) + "0")
        else:
            print(str(i) + ":" + str(j))

"""
# II.Szótár gyakorlás

# 1. feladat

"""
lista = []

nev = input("Add meg a nevedet: ")
kor = int(input("Add meg a korodat: "))
nem = input("Add meg a nemedet: ")
menza = int(input("Ha menzás vagy írj egyest: "))

if menza == 1:
    menza = "Menzás"
else:
    menza = "Nem menzás"

lista.append(nev)
lista.append(kor)
lista.append(nem)
lista.append(menza)
print(lista)
"""

# 2. feladat
"""
import random # Ezt ne hagyjuk ki :)

naplo = {'Vezetéknév': input("Add meg a vezetéknevedet: "),
         'Keresztnév': input("Add meg a keresztnevedet: "),
         'Cím': input("Add meg a címedet: "),
         'Évfolyam': random.randint(9, 12),
         'Osztály': input("Add meg az osztályodat: ")
}
print(naplo['Vezetéknév'])
print(naplo['Keresztnév'])
print(naplo['Cím'])
print(naplo['Évfolyam'])
print(naplo['Osztály'])
"""
# Nem tudom hogy hogy lehet ismételni

#2. és 3. feladat egyben.
diak = {}
naplo = []
ok = True
l = 0

while ok:
    print(str(l + 1) + ". számú diák adatai:")
    diak = {
        'Vezetéknév': input("Add meg a vezetéknevedet: "),
        'Keresztnév': input("Add meg a keresztnevedet: "),
        'Cím': input("Add meg a címedet: "),
        'Évfolyam': random.randint(9, 12),
        'Osztály': input("Add meg az osztályodat: ")
    }
    naplo.append(diak)
    diak = {}
    l += 1
    if l == 8:
        ok = False

valasz = int(input("Szereténél módosítani a naplóban? 1 - igen, 0 - nem: "))

if valasz == 0:
    print("Akkor viszlát!")
else:
    print("Kérem adja meg hogy mi a gyermeke vezetékneve és azt hogy egy melyik értéket módosítaná(1-5) és mivé!")
    #Feltételezem, nincs ugyanolyan nevű gyerek és hogy az öcskös jó kulcsot ír be!
    gyerek_neve = input("Név: ")
    kulcs_neve = int(input("Módosítandó rész sorszáma: "))
    modos = input("Mit írjak a régi érték helyére: ")

for i in naplo:
    if i['Vezetéknév'] == gyerek_neve:
        if kulcs_neve == 1:
            i['Vezetéknév'] = modos
        elif kulcs_neve == 2:
            i['Keresztnév'] = modos
        elif kulcs_neve == 3:
            i['Cím'] = modos
        elif kulcs_neve == 4:
            i['Osztály'] = modos


print('A módosított napló:')
for i in naplo:
    print(i)

# 3. fekadat sem ment

#III.Beolvasás
