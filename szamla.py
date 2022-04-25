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
        for y in range(len(adatok[i])):
            adatok[i][y]=int(adatok[i][y])
    print(adatok)
    #telefonszám, kezdő óra, kezdő perc, kezdő másodperc
beolvasas()
#1.


















#2.



















#3.



















#4.



















#5.



















