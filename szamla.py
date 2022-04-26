#1.feladat
tel=str(input("Kérek egy telefonszámot!\n"))
if tel[0:2]=="39" or tel[0:2]=="41" or tel[0:2]=="71":
    print("Ez a szám mobilhívószám!")
else:
    print("Ez a szám vezetékes hívószám!")
#2.feladat
kezd=input("Kérek egy hívás kezdeti időpontot! <ó p m>\n")
veg=input("Kérek egy hívás vége időpontot! <ó p m>\n")
def idokul(kezd, veg):
    from datetime import datetime
    ss="%H %M %S"
    kul=datetime.strptime(veg,ss)-datetime.strptime(kezd,ss)
    secs=kul.seconds
    mins=int((secs+60)/60)
    return mins
mins=idokul(kezd, veg)
print("Ez a hívás",mins,"percig tartott!")
#3.feladat















































#4.feladat







































#5.feladat















































#6.feladat