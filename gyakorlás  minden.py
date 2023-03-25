#I rész
# 1. feladat
import math

lista = [-2, 3, 7]
max = lista[0]
min = lista[0]
for i in lista:
    if i > max:
        max = i
    if i < min:
        min = i
print(f"Legnagyobb szám: {max}")
print(f"Legkisebb szám: {min}")
#Nem erre gondoltam de így még tökéleteseb. A math-nak van min és max fg.-je

#2. feladat

for i in lista:
    if min < 0:
        abszolut = abs(min)
print(abszolut)
#Jó lesz csak ebben az esetben felesleges a for ciklus mivel csak egy számra voltam kíváncsi. Így viszont mindig csak az utolsó lesz benne
#ami végülis jó. 

#3. feladat

szam = 2**5
print(szam)
#Teljesen jó

#4.feladat
print(math.sqrt(1024))
#Perrfect!

#5 feladat
print(round(9.65))
#Ez alapjáraton egészre kerekít
#math.ceil(1.4) --> Ez kerekít felfele ami azt jelenti hogy az output 2 lesz
#math.floor(1.4) --> Ennek meg az otputja 1 lesz


#6. feladat
pi = math.pi
print(pi, type)
#Jó!

print("------------------")
#II rész
#1. feladat

lista1 = ["zöld", "kék", "piros"]
for index, elem in enumerate(lista1):
    print(f"{index}. {elem}")
print()
#Jó!
#2. feladat
for index, elem in enumerate(lista1):
    print(f"{index+1}. {elem}")
print()
#Jó!
#3. feladat
lista2 = [2, 4, 5, 7, 8]
for index, elem in enumerate(lista2):
    if elem % 2:
        print(f"{index + 1}. {elem} ")
    else:
        print(f"{index + 1}. {elem}+")
 #Ez így jó csak én arra gondoltam hogy a string listának a sorszámainál ahol páros van, ott legyen egy +. Viszont ez is teljesen jó. Látszik hogy érted!
print("-----------------------------------")
#III. rész
#1.feladat
beker = int(input('Írj be egy 0-át: '))
while beker != 0:
    while beker < 0 or beker > 0:
        print("Nem jó")
        beker = int(input('Írj be egy 0-át: '))
    break
#Szuper!
#2. feladat
szam = int(input("Adj meg egy számot: "))
#?
"""
Szám visszafele:
num = int(input("Adj meg egy számot:"))
rev = 0

while num != 0:
    r = num%10
    rev = rev * 10 + r
    num = num // 10


print(rev)

"""



#3. feladat
for i in range(1, 10):
    print(i, i**2)
#Jó!

#4. feladat
"""
szam = int(input("Adj meg egy számot: "))
b = 0
p = 1
n = szam

while n > 0:
    tmp = n%2
    b += tmp * p
    p = p*10
    n = n//2

print(b)
"""
print("------------------------------")

#IV. rész
#1. feladat

Peti_kedvencei = {'halászlé', 'bécsi szelet', 'bukta', 'rakott krumpli', 'almás rétes' }
Kriszti_kedvencei = {'borsóleves', 'bécsi szelet', 'túrós tészta', 'lecsó', 'almás rétes' }

print(len(Peti_kedvencei & Kriszti_kedvencei))
print(Peti_kedvencei & Kriszti_kedvencei)
print()
print(len(Peti_kedvencei - Kriszti_kedvencei))
print(Peti_kedvencei - Kriszti_kedvencei)
print()
print(Peti_kedvencei ^ Kriszti_kedvencei)
print(len(Peti_kedvencei ^ Kriszti_kedvencei))
print("----------------------------------")
#V. rész
#1. feladat

def szamok(szam1, szam2):
    return szam1, szam2

print(szamok(3, 11))

def szamok1(szam1, szam2):
    if 0 < szam1 < 10 and 0 < szam2 < 10:
        print('benne van')
    elif 0 < szam1 < 10 or 0 < szam2 < 10:
        print("csak az egyik van 1 és 10 között")
    else:
        print("nincs benne")
    return szam1, szam2

print(szamok1(3, 11))

def szamok2(x, y):
    osszeg = x + y
    return osszeg

print(szamok2(3, 5))

def szamok3(x, y):
    if x > y:
        eredmeny = x - y
    else:
        eredmeny = y - x
    return eredmeny
print(szamok3(14, 5))




"""
def x_bekeres():
    x = int(input("szam: "))
    return x

def y_bekeres():
    y = int(input("szam: "))
    return y

x = x_bekeres()
y = y_bekeres()


def szamok1(szam1, szam2):
    if 0 < szam1 < 10 and 0 < szam2 < 10:
        print('benne van')
    elif 0 < szam1 < 10 or 0 < szam2 < 10:
        print("csak az egyik van 1 és 10 között")
    else:
        print("nincs benne")





print(szamok1(x, y))

def szamok2(x, y):
    osszeg = x + y
    return osszeg

print(szamok2(x, y))

def szamok3(x, y):
    if x > y:
        eredmeny = x - y
    else:
        eredmeny = y - x
print(szamok3(x, y))


"""






