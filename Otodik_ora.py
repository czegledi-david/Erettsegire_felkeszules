#Fg == Függvény csak lusta vagyok kiírni ¯\_(ツ)_/¯

#Függvények és eljárások
"""
A függvényeket és eljárásokat a def kulcsszóval hozzuk létre. A különbség hogy a fügvények egy értékkel
térnek vissza. (return kulcsszó)
"""
#Eljárás példa
def koszont():
    print("Hello World!")

"""
Ha ezt meghívod akkor szekvenciálisan (fentről, lefelé) lefut majd ennyi. 
"""
#Ez is eljárás
def osszead(x,y): #<-- Paraméterek
    eredmeny = x + y
    print('A két szám összege: ', eredmeny)

"""
Ami nagyon fontos, attól hogy ennek az eljárásnak van paramétere és számol, attól még ez nem fg.
Ha a return kulcsszót látod, akkor beszélünk fg.-ről.
"""

#Fg. példa:
def Szorzas(x, y):
    eredmeny = x * y
    return eredmeny


"""
Ugyanúgy kell létrehozni mint egy eljárást, csak itt kapunk egy visszatérési értéket amivel a fő programban
(main) tudunk tovább számolni.
"""

#Paraméterekről részletesen. Olvassd el! Csak érdekesség gyanánt.
#https://tudasbazis.sulinet.hu/hu/informatika/informatika/informatika-9-12-evfolyam/alprogramok/alprogramok-parameterei
#Meghívások
koszont()
a = 3
b = 12
#Összeadja a két számot!
osszead(a, b)
#A szorzás és erre egy külön változót is létrehozok hogy a return értéket eltudjam menteni!!!!!!!!!
eredmeny = Szorzas(a, b)

print(eredmeny)
# EZT CSAK AKKOR HA MÁR MENNEK A FENTIEK!
# Így is átlehet adni paraméterek ha konkrétan leírod hogy kinek mit
# Ha nem adod meg akkor balról-jobbra fogja
# Szóval az 52. sor ugyanazt csinálja mint a 45. sor az egyenlőség jel után!
print(Szorzas(x=a, y=b))

"""
Nem kell mindet(bár nem hátrány persze), a lányeg hogy csinálj belőlük mert csak úgy tanuéja meg az ember ha csinálja!

Feladatok:
1. Feladat
Írj eljárást, amely egy tetszőleges szöveget, ill. alakzatot ír ki a képernyőre!

2. Feladat
Írj eljárást, amely paraméterül kapott 2 számot összehasonlít, és a képernyőre kiírja, melyik a nagyobb szám!
Kezeld azt az esetet is, ha a két szám egyenlő!


3. Feladat
Írj egy programot, amely tartalmaz egy 'osszegzo' nevű függvényt, ami a paraméterként átvett listaelemeket
(egész számokat) összeadja és az összegükkel tér vissza! A program tartalmazza a függvény hívását is!

A két négyes már nehéz. ⚆ _ ⚆
Ha nem mennek nem gáz! 

4. Feladat
Írj egy programot, ami addig kér be egész pozitív számokat, amíg a felhasználó negtív számot nem ír!
A megadott számokat tárolja a program egy listában, és ezt adja át paraméterként egy függvények,
amely a lista legkisebb elemével tér vissza. A program írja ki, hogy melyik volt a megadott legkisebb szám!

4. Feladat - Ez már egy kicsit nehéz
Írj egy programot, amely a felhasználótól bekér 3 szót, ezeket egy listában tárolja, és egy eljárás segítségével
meghatározza, és a képernyőre kiírja, melyik a legrövidebb szó!
"""
