#1. Adattípusok

#Listában listák

homersekletek = [] #- Ez egy sima üres lista

pentek = [11, 19, 17] #- Ez is egy sima üres lista
szombat = [13, 20, 14] #- Ez is egy sima üres lista
vasarnap = [10, 15, 9] #- Ez is egy sima üres lista

homersekletek.append(pentek) #Listába teszünk elemet de ezt tudod
homersekletek.append(szombat)#--||--
homersekletek.append(vasarnap)#--||--

print(homersekletek[0]) # Az érdekes része itt kezdődik
#Ugyanis itt a pentek nevű listát íratja ki, vagyis: [11, 19, 17]

#Szótár
raktar = {} #Szótárt hozz létre - nem összekeverendő a halmazzal!!!!! A halmazt majd később taglalom

#Úgy képzeld el a halmazt mint egy excel táblát, csak itt kulcs és érték van.
raktar = {
#          KULCS       ÉRTÉK
        'vezeteknev': 'Kiss',
        'keresztnev': 'Ádám',
         'eletkor': 18,
         'menza': True
}

#Szótár indexelése!!!

print(raktar['vezeteknev']) #Ezzel kiírja a kulcshoz kapcsolodó értéket

print("_-_-_-_")
print(raktar.get('menza'))  #True vagy False értéket fog vissza adni.

print("_____")
print('keresztnev' in raktar) # True vagy false.

raktar['eletkor'] = 19 #Ezzel módosítunk értéket csak így szimplán
print(raktar['eletkor'])

del raktar['menza'] #Törlés- Ekkor törli a kulcsot és a hozzá tartozó értéket is.

#Az egész szótárat kiírja!- Szimpla for ciklus.
for i in raktar:
    print(i, raktar[i])


#Halmazok

reggeli = {'tea', 'vaj', 'kenyér'} #- Létrehoz egy hamlazt

"""
ebed = {}
^
Szótárt hoz létre. Hiába nem írsz bele kulcsot és értéket attól még ez szótárként lesz deklarálva!
"""

#Ha üres halmazt akarsz létrehozni akkor a 61.sor a te sorod. Ez fontos!
ebed = set()

#Elemet így tudsz hozzáadni vagy törölni.
ebed.add('leves')
ebed.remove('leves')

ebed = {'leves', 'halászlé', 'víz', 'kenyér'} #Vagy így

#metszet
print(reggeli & ebed) #reggeli ∩ ebed - a közös elem
#unio
print(reggeli | ebed)#-----
#reggeli U ebed - Az összes elem. Mindet kiírja ami reggeliben és ebédben és a közösben is benne van


#különbség
print(reggeli - ebed) # reggeli \ ebed - Csak a reggeli elemeit írja ki!
# csak az egyikben, vagy csak a másikban
print(reggeli ^ ebed) # Csak a reggeli és az ebéd elemeit írja ki. A közös elemeket nem!

#2. Fájlkezelés

"""
Úgy fogom írni ahogy én tanultam de mivel ti máshogy csináljátok(lehet 100 féle képpen) ezért majd ha látom hogy ti
hogyan toljátok akkor átírom!
"""

# fajl megnyitása
forrasfajl = open('/home/david/Downloads/adatok.txt') #Példa fájl.

# fájl tartalmának beolvasása
# egy sor beolvasása:
forrasfajl.readline()

# a teljes fájltartalom beolvasása
# listával tér vissza, a sorok a lista elemei
forrasfajl.readlines()

# a teljes fájltartalom beolvasása
forrasfajl.read()

# a fájlobjektum tartalmanak bejarasa
for sor in forrasfajl:
    print(sor)

# fájl bezárása
forrasfajl.close() #Ez egy nagyon fontos sor. Ha befejezted a fájlműveleteket akkor mindig zárd le mert mindent amit
#írsz utána akkor az a fájlba megy!

#Ettől majd még később csak ide rakom!
autok = []
with open('adatok/autok_listaja.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(',')
        auto = {'rendszam': adatok[0], 'tipus': adatok[1], 'kor': int(adatok[2])}
        autok.append(auto)

print(f'{autok=}')