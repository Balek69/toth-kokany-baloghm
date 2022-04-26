#1 feladat:





























































#2 feladat:













































#3.feladat








































#4.feladat











































#5.feladat
file.seek(0)
def mobile(szam):
#Ha mobilszám akkor 1-et, ha nem 0-át ad vissza.
    if szam[0:2]=="39" or szam[0:2]=="41" or szam[0:2]=="71":
        return 1
    else:
        return 0

def idokulsor(sor):
    from datetime import datetime
    kezdi=elemek[0:3]
    vegi=elemek[3:6]
    kezdd=" ".join(kezdi)
    vegg=" ".join(vegi)
    ss="%H %M %S"
    kul=datetime.strptime(vegg,ss)-datetime.strptime(kezdd,ss)
    secs=kul.seconds
    mins=int((secs+60)/60)
    return mins

mobilperc=0
vezperc=0
k=0
a=file.readlines()
while k<len(a):
    if k%2==1:  #telefonszám
        if mobile(a[k]):  #Ha mobil
            mobilperc=mobilperc + idokulsor(a[(k-1)])
        else:
            vezperc=vezperc + idokulsor(a[(k-1)])
    k=k+1
print("A felhasználó vezetékkesel",vezperc, "percet, mobillal",mobilperc,"percet beszélt.")

#6.feladat
def csucse(sor):
#1-et ad vissza, ha csúcsidőben van. 0-t ha nem.
    elemek=sor.split()
    kezdi=elemek[0]
    vegi=elemek[3]
    if int(kezdi)>=7 and int(kezdi)<18:
        return 1
    else:
        return 0

file.seek(0)
a=file.readlines()
b=0
mobperc=0
vezperc=0
while b<len(a):
    if b%2==0:  #Időpontok          
        if csucse(a[b]):
            if mobile(a[(b+1)]):
                mobperc=mobperc+ idokulsor(a[b])
            else:
                vezperc=vezperc+idokulsor(a[b])
    b=b+1

fizetni=float(mobperc)*69,175 + float(vezperc)*30
print("A felhasználónak a csúcsdíjas hívásokért összesen", fizetni, "Ft-ot kell fizetnie.")
#vége