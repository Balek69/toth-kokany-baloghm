adatok=[]
def beolvasas():
    #megnyitja
    r=open("hivasok.txt","r",encoding="UTF-8")
    e=r.readline()
 
    m=e

    e=r.readline()

    sor = e.strip()+ " " + m.strip()

    #beolvas egy sort, azt eltárolja, majd beolvas még egyet, azokat egy sorrá teszi, majd beolvassa a listába az egy sort mint egy lista, magyarán lista listában
    adatok.append(sor.split(" "))
    while e:
        e=r.readline()
        m=e
        e=r.readline()
        sor = e.strip()+ " " + m.strip()

        adatok.append(sor.split(" "))
    del(adatok[-1])
    #inté teszi őket
    for i in range(len(adatok)):
        for y in range(1,len(adatok[i])):
            adatok[i][y]=int(adatok[i][y])

    #telefonszám, kezdő óra, kezdő perc, kezdő másodperc
beolvasas()
#1.
szam=input("Mondj egy telefonszámot: ")
letezik=False
if szam[0:2]=="39" or szam[0:2]=="41" or szam[0:2]=="71":
    for i in range(len(adatok)):
        if adatok[i][0]==szam:
            letezik=True
            break
    if letezik:
        print("Létező mobilszám!")
    else:
        print("Nem létező mobilszám!")
else:
    print("Nem mobilszám!")



#2.
hivas=[]
hivas.append(int(input("Hívás eleje: óra: ")))
hivas.append(int(input("Hívás eleje: perc: ")))
hivas.append(int(input("Hívás eleje: másodperc: ")))
hivas.append(int(input("Hívás vége: óra: ")))
hivas.append(int(input("Hívás vége: perc: ")))
hivas.append(int(input("Hívás vége: másodperc: ")))

print(f"{((hivas[3]-hivas[0])*60)+(hivas[4]-hivas[1])} perc hosszúság volt a hívás.")

#3.



















#4.



















#5.



















