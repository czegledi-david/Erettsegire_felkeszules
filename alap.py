#2022-11-12 - 1.óra

#1.STRINGEK:
"""
Elmélet:
A karaktersorozatok (un. sztringek)
megadásakor használhatunk aposztrófot vagy idézőjelet, mind a kettő használata megengedett.
"""
#Példa:
print("Idézőjelek közé írva!")
print('Aposztrófok közé írva')

#2.KOMMENTEK:
#Egysoros komment

""""
Több soros komment!
!Ha kommentbe írsz kódot az nyílvánvalóan nem fog lefutni!
"""

#3.VÁLTOZÓK
"""
Fontos hogy a változók típusát nem mi adjuk meg hanem a fordító!
Ezért a python egy gyengén típusos nyelv! Ha érdekel ennek a hosszú
elemzése akkor úgy keress rá hogy 
Erős és Gyenge típusos nyelvek különbsége! Ha van kérdés majd ezzel jelezz!:)
"""
szam = 5 #Ez egy int(egész szám) típusú változó
"""
!A szam az AZONOSÍTÓ!
!Az 5 pedig az ÉRTÉK!
"""

szoveg = 'Alma' #Ez egy string(szöveg) típusú változó
szoveg2 = 'Alma' #Ez egy szöveg(szöveg) típusú változó
"""
Mind a kettő jó!
!A szoveg az AZONOSÍTÓ!
!Az alma pedig az ÉRTÉK!
"""

tizedes_szam = 12.5 #Ez egy double/float(tizedes szám) típusú változó
"""
!A tizedes_szam az AZONOSÍTÓ!
!Az 12.5 az ÉRTÉK!
"""

logikai_valtozo = True #Ez egy bool(logikai) tipusú válzotó
#Két értéke lehet: True vagy False (Igaz vagy Hamis)
"""
!A logikai_valtozo az AZONOSÍTÓ!
!A True az ÉRTÉK!
"""

#Változók kiíratása:
"""
Ha a változók egy magukban akarjuk kiírni akkor elég csak a nevét kiírni:
print(valtozo_neve)
Viszont ha szöveggel akarjuk akkor a következő képen lehet:
print("A korod: " + str(valtozo_neve)) <-- STRINGGÉ KELL KONVERTÁLNI!
"""

#Érdekességek:
"""
1. Ha megakarod nézni hogy egy változódnak mi az értéke akkor egy sorral meglehet nézni:
Link hozzá: https://replit.com/@sulipy/valtozok-pl02#main.py
2. Ha egy változót csupa nagybetűvel írsz akkor az konstans(nem tudod módosítani)
pl.: PI = 3.14
"""


#4.Matematikai műveletek és adatbekérés
#Számbekérés:
adat = input('Adj meg egy számot! ')
szam = int(adat)
"""
Mivel az input függvény mindig sztringet ad vissza,
ha számot kérsz be, ne feledkezz meg a típusátalakításról!
"""

#rövidebben:
szam = int(input('Adj meg egy számot! '))
#Ezt használtuk órán is. Gyorsabb és nem lesz fölösleges szemét
#Persze az elsőt is használhatod érettségiben is!

#Matematikai műveletek
x = 7
y = 3
#összeadás
print(x + y)
#kivonás
print(x - y)
# szorzás
print(x * y)
#osztás
print(x / y)
# maradékos osztás, az osztás maradékát adja eredményül
print( x % y)

#Stringek összefűzése
szo1 = 'alma'
szo2 = 'fa'
print(szo1 + szo2)
#Output: almafa!

#5.Elágazások

#Összehasonlító operátorok
"""
x = 2
y = 4
1. x == y - Megnézi hogy a két változó értéke egyenlő-e! 
2. x != y - Nem egyenlőséget néz! Az ellentétje az előzőnek!
3. x < y - Megnézi hogy az x kisebb-e mint az y
4. x > y -  Megnézi hogy az x nagyobb-e mint az y
5. x <= y - Megnézi hogy az x kisebb VAGY egyenlő-e!
*Ha kisebb akkor is lefut és ha egyenlő akkor is. Elég ha az egyik igaz*

6. x >= y - Megnézi hogy az x nagyobb-e VAGY egyenlő-e!
*Ugyanaz mint az ötösnél!*
"""

#Logikai operátorok
"""
And, Or és not(A not-ot nagyon ritkán használjuk. Csak lássd ilyen is van)
"""

#AND
if x < 0 and y < 0: #Itt mindakettőnek igaznak kell lennie. Ha az egyik nem teljesül akkor nem lesz kiírva a szöveg
    print("Mindakettő negatív")

#OR
if x < 0 or y < 0: # Itt elég ha az egyik igaz. Akkor is lefog futni!
    print('van köztük negatív')

#NOT (Csak érdekesség)
if not x <= 0:
    print('x pozitív')

#6.Random számok

#Nagyon fontos. A Random számokhoz importálni kell a random csomagot(Asszem csomagnak hívják)
#Általában az első sorok egyikébe kell írni: import random
import random
#Ide is lehet de te mindenképpen fentre írd!! Bele köthetnek!!

random_szam = random.randint(1, 10) #Ebben benne van az 1 és a 10 is!!
random_szam2 = random.randrange(1, 11) #Ebben is benne van az 1 és a 10 is csak ha range van akkor 11-ig kell menni ha
# a 10 is kell!
print(random_szam)
print(random_szam2)