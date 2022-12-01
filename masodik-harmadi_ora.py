#while magyarul azt jelenti: amíg
szam = 1
while szam <= 10:
    print(szam)
    szam = szam + 1

"""
Ez a program 1-10-ig írja ki a számokat
Ugyanúgy meglehet csinálni for ciklussal is! 
"""
print("")
for i in range(1, 11):
    print(i)

#Pl egy órai feladat:
folytatja = True
while folytatja: #Ez azt jelenti hogy addig meg amíg a folytatja igaz.(folytatja == True)
      print('Vidd ki a szemetet!')
      valasz = input('Mondjam még egyszer? (i/n)')
      if valasz == 'n':
        folytatja = False
print('>> Program vége! <<')

#Listák
#lista létrehozása:
#indexek: 0  1  2  3  4
szamok = [1, 2, 3, 4, 5]
#szavas lista:
#indexek:    0       1         2         3
szavak = ['alma', 'körte', 'barack', 'dinnye']

#A lista bárhanyadik indexét letudod kérdezni:
print(szavak[2]) #A barackot fogja kiírni
#Ki írja a listát
print(szavak)
#Szebben írja ki a listát vesszővel elválasztva :)
print(', '.join(szavak))
#A lista hosszát írja ki
print(len(szamok))
"""
Van egy nagyon fontos szabály
Tudd hogy hány elemű a lista
Gondolj bele
Elindítassz egy for ciklust 5-ig de a listád 4 elemű és elkezdel gondolkodni hogy mi az isten van, miért nem megy amivel idő telik 
(｢•-•)｢ ʷʱʸ?

Azt fogja kiírni hogy túlindexelés történt.
Ilyenkor szimplán írd be hogy print(len(szamok))
Ilyenkor kidobja az elem számot és azt írod a forba.
"""
#Órai feladat
 # üres listát hoz létre
gyumolcsok = []

gyumolcs = None # kezdőérték nélküli változót hoz létre
while gyumolcs != '':
  gyumolcs = input('Adj meg egy gyümölcsöt! ')
  if gyumolcs != '':
      # hozzáfűzi a listahoz
      gyumolcsok.append(gyumolcs)
  
print(gyumolcsok)

#Összegzés tétele
#Órai feladat
napi_ertekesitesek = [3, 12, 3, 4, 7, 15, 1]
osszesen = 0
for ertekesites in napi_ertekesitesek:
    osszesen = osszesen + ertekesites # Ez az összegzés tétele
    #osszesen += ertekesitis - rövidebb ( ಠ ͜ʖಠ)

print("A héten ennyi értékesítés történt: ", osszesen)

#Megszámlálás tétele
"""
A SZÁMLÁLÁS esetében azt vizsgáljuk, hogy egy bizonyos tulajdonságú elemből 
hány darab van az adatsorban (itt a listában).
¯\_(ツ)_/¯
A program azt vizsgálja, hogy hány darab hárommal osztható szám van a listában.
"""
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]
darab = 0
for szam in lista:
    if szam % 3 == 0:
        darab = darab + 1

print('A listában lévő hárommal osztható számok száma: ', darab)

#Szélsőérték meghatározása - Minimum, maximum
"""
A SZÉLSŐÉRTÉK MEGHATÁROZÁSA esetében azt vizsgáljuk, hogy melyik a legkisebb, illetve a legnagyobb érték az adatsorban
(itt a listában).
(͡• ͜໒ ͡• )
"""
lista = [12, 5, 4, 8, 9, 11, 10, 12, 6]

min = lista[0]
max = lista[0]
for szam in lista:
    if szam < min:
        min = szam
    if szam > max:
        max = szam

print('A legkisebb szám a listában: ', min)
print('A legnagyobb szám a listában: ', max)


"""
Feladatok:
1.Készíts egy programot, amely a felhasználótól számokat kér be mindaddig, amíg az csupán ENTER-t nem üt!
A számokat tárolja el a program egy listában!
Az adatbekérés befejezte után írja ki a program a lista elemeit, a legkisebb és a legnagyobb számot!

2.Alakítsd át úgy az előbbi programot, hogy az 'X' vagy 'x' megadása eredményezze az adatbekérés végét!

3.Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában!
A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit!
"""

