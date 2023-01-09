from math import *

#1
print("1 Harjutus")
nimi = input("Mis sinu nimi on? ")
while nimi.isalpha()==False:
    nimi= input("Palun kirjuta õige nimi - ")
if nimi.lower() == "juku":
    print("Läheme kinno!")
    age = input("Kui vana sa oled? ")
    while age.isdigit()==False or int(age)!=float(age) or int(age)==0 or int(age)>=100:
        age=input("Kirjuta õiges vanus! - ")
    age=int(age)
    if age<6:
        print("Sinu pilet on tasuta")
    elif age>=6 and age<14:
        print("Sinu pilet on lastpilet")
    elif age>=15 and age<=65:
        print("Sinu pilet on täispilet")
    else:  
        print("Sinu pilet on sooduspilet")
else:
    print("Ilus nimi")

#2
print("")
print("2 Harjutus")
naber1=input("1 inimene, mis sinu nimi on? ")
while naber1.isalpha()==False:
    naber1=input("Palun kirjuta õige nimi - ")
naber2=input("2 inimene, mis sinu nimi on? ")
while naber2.isalpha()==False:
    naber2=input("Palun kirjuta õige nimi - ")
if naber1.lower() in ["timur","juku"] and naber2.lower() in ["juku","timur"]:
    print(f"{naber1} ja {naber2} te olete nüüd naabrid")
else:
    print("Head nimed!")

#3
print("")
print("3 Harjutus")
kp1=input("Ristkülikukujulise põranda esimese külje pikkus - ")
while kp1.replace(".","",1).isdigit()==False or float(kp1)==0:
    print("Palun kirjuta õige number")
    kp1=input("Ristkülikukujulise põranda esimese külje pikkus - ")
kp2=input("Ristkülikukujulise põranda teiseks külje pikkus - ")
while kp2.replace(".","",1).isdigit()==False or float(kp2)==0:
    print("Palun kirjuta õige number")
    kp2=input("Ristkülikukujulise põranda teiseks külje pikkus - ")
kp1=float(kp1)
kp2=float(kp2)
S=kp1 * kp2
print(f"Teie põrandapind - {S}")
remont=input("Kas soovite põrandat renoveerida? (jah või ei) ").lower()
while remont not in ["jah","ei"]:
    remont=input("Palun kirjuta jah või ei - ").lower()
if remont=="jah":
    hind=input("Kui palju maksab üks ruutmeeter eurodes? ")
    while hind.replace(".","",1).isdigit()==False or float(hind)==0:
        hind=input("Kirjuta õige hindes ")
    hind=float(hind)
    hindS = hind * S
    print(f"Remondi hind - {hindS} euro")
else:
    print("Kahju, tulge kui soovite remonti teha!")

#4
print("")
print("4 Harjutus")
hind = input("Palju ese maksab? ")
while hind.replace(".","",1).isdigit()==False or float(hind)==0:
    hind=input("Kirjuta õige hind! ")
hind=float(hind)
if hind>700 :
    hindP= (hind * 30)/100
    print(f"Sinu allahindlust on {hindP}")
else:
    print("Sulle allahindlust ei tehta!")

#5
print("")
print("5 Harjutus")
grad=input("Mis on temperatuur majas? ")
while grad.replace(".","",1).replace("-","",1).isdigit()==False :
    grad=input("Kirjuta õige temperatuur! ")
grad=float(grad)
if grad>=18:
    print("Suurepärane temperatuur!")
else:
    print("Lülitage patareid sisse!")

#6
print("")
print("6 Harjutus")
pikkus=input("Kui pikkus sa oled? ")
while pikkus.replace(",","",1).isdigit()==False or int(pikkus)!=float(pikkus) or float(pikkus)<70 or float(pikkus)>250:
    pikkus=input("Kirjuta õige pikkus! ")
pikkus=float(pikkus)
if pikkus<=150:
    print("Sa oled lühike")
elif pikkus>150 and pikkus<=180:
    print("Sa oled keskmine")
else:
    print("Sa oled pikk")

#7
print("")
print("7 Harjutus")
sugu=input("Kas sa oled mees või naine? ").lower()
while sugu not in ["mees","naine"]:
    sugu=input("Kirjuta õige sugu!")
pikkus=input("Kui pikkus sa oled? ")
while pikkus.replace(",","",1).isdigit()==False or int(pikkus)!=float(pikkus) or float(pikkus)<70 or float(pikkus)>250:
    pikkus=input("Kirjuta õige pikkus! ")
pikkus=float(pikkus)
if sugu=="mees":
    if pikkus<165:
        print("Sa oled lühike mees")
    elif pikkus>=165 and pikkus<185:
        print("Sa oled keskmine mees")
    else:
        print("Sa oled pikk mees")
else:
    if pikkus<150:
        print("Sa oled lühike naine")
    elif pikkus>=150 and pikkus<170:
        print("Sa oled keskmine naine")
    else:
        print("Sa oled pikk naine")

print("Midagi on vale")

#8

print("")
print("8 Harjutus")
piima=input("Kas sa tahad osta piima? (jah või ei) ").lower()
while piima not in ["jah", "ei"]:
    piima=input("Kirjuta ainult jah või ei! ").lower()
if piima=="jah":
    hindPiima=input("Kui palju maksab piima? ")
    while hindPiima.replace(",","",1).isdigit==False or hindPiima==0:
        hindPiima=input("Kirjutage õige hind! ")
    kogusPiima=input("Kui palju sa tahad osta? ")
    while kogusPiima.isdigit()==False or kogusPiima==0:
        kogusPiima=input("Kirjuta õige arv! ")
sai=input("Kas sa tahad osta sai (jah või ei) ").lower()
while sai not in ["jah", "ei"]:
    sai=input("Kirjuta ainult jah või ei! ").lower()
if sai=="jah":
    while (hindSaiE+hindSaiC/100)<=0:
        print("Kogusumma peab olema suurem kui null")
        hindSaiE=input("Kui palju maksab Sai? (Terve tükk eurost) ")
        while hindSaiE.isdigit()==False:
            hindSaiE=input("Palun kirjuta õige hind! ")
        hindSaiC=input("Kui palju maksab Sai? (Saldo sentides) ")
        while hindSaiC.isdigit()==False or float(hindSaiC)>=100:
            hindSaiC=input("Palun kirjuta õige hind! ")
        kogusSai=input("Kui palju sa tahad osta? ")
        while kogusSai.isdigit()==False or int(kogusSai)!=float(kogusSai) or int(kogusSai)<=0:
            kogusSai=input("Kirjuta õige number kui palju sa tahad osta Sai! ")
        hindSaiE=float(hindSaiE)
        hindSaiC=float(hindSaiC)
        kogusSai=int(kogusSai)
    hindSai=hindSaiE+hindSaiC/100
leib=input("Kas sa tahad osta leib (jah või ei) ").lower()
while leib not in ["jah", "ei"]:
    leib=input("Kirjuta ainult jah või ei! ").lower()
if leib=="jah":
    while (hindLeibE+hindLeibC/100)<=0:
        print("Kogusumma peab olema suurem kui null")
        hindLeibE=input("Kui palju maksab Leib? (Terve tükk eurost) ")
        while hindLeibE.isdigit()==False:
            hindLeibE=input("Palun kirjuta õige hind! ")
        hindLeibC=input("Kui palju maksab Leib? (Saldo sentides) ")
        while hindLeibC.isdigit()==False or float(hindLeibC)>=100:
            hindLeibC=input("Palun kirjuta õige hind! ")
        kogusLeib=input("Kui palju sa tahad osta? ")
        while kogusLeib.isdigit()==False or int(kogusLeib)!=float(kogusLeib) or int(kogusLeib)<=0:
            kogusLeib=input("Kirjuta õige number kui palju sa tahad osta Leib! ")
        hindLeibE=float(hindLeibE)
        hindLeibC=float(hindLeibC)
        kogusLeib=int(kogusLeib)
    hindLeib=hindLeibE+hindLeibC/100
if piima=="ei" and sai=="ei" and leib=="ei":
    print("Ostude summa on 0")
elif piima=="ei" and sai=="ei" and leib=="jah":
    OS=hindLeib * kogusLeib
    print(f"Ostude summa on {OS}")
elif piima=="ei" and sai=="jah" and leib=="ei":
    OS=hindSai * kogusSai
    print(f"Ostude summa on {OS}")
elif piima=="ei" and sai=="jah" and leib=="jah":
    OS=hindSai * kogusSai + hindLeib * kogusLeib
    print(f"Ostude summa on {OS}")
elif piima=="jah" and sai=="ei" and leib=="ei":
    OS=hindPiima * kogusPiima
    print(f"Ostude summa on {OS}")
elif piima=="jah" and sai=="ei" and leib=="jah":
    OS=hindPiima * kogusPiima + hindLeib * kogusLeib
    print(f"Ostude summa on {OS}")
elif piima=="jah" and sai=="jah" and leib=="ei":
    OS=hindPiima * kogusPiima + hindSai * kogusSai
    print(f"Ostude summa on {OS}")
else:
    OS=hindPiima*kogusPiima + hindSai*kogusSai + hindLeib*kogusLeib
    print(f"Ostude summa on {OS}")

print("Midagi on vale")

#9

print("")
print("9 harjutus")
print("Kirjutage täisarvud (kui väärtus ei ole täisarv, teisendage muudeks mõõtmisteks)")
a=input("Kirjutage 1 külje pikkus - ")
while a.isdigit()==False:
    a=input("Kirjuta õige pikkus ")
b=input("Kirjutage 2 külje pikkus - ")
while b.isdigit()==False:
    b=input("Kirjuta õige pikkus ")
if a==b:
    print("See on ruut!")
else:
    print("See ei ole ruut!")

print("Midagi on vale")

#10

print("")
print("10 harjutus")
a=float(input("Kirjutage esimene number "))
b=float(input("Kirjutage teine number "))
s=input("Kirjutage tegevuse märk (+ - * /) ")
while s not in ["+","-","*","/"]:
    s=input("Kirjutage ainult see tegevuse märk (+ - * /) ")
if s=="+":
    t=a+b 
    print(f"Tegevuse tulemus on {t}")
elif s=="-":
    t=a-b
    print(f"Tegevuse tulemus on {t}")
elif s=="*":
    t=a*b 
    print(f"Tegevuse tulemus on {t}")
else:
    if b>0 and b<0:
        t=a/b
        print(f"Tegevuse tulemus on {t}")
    else:
        print("Nulliga jagada ei saa.")

print("Sa ei kirjutanud numbreid.")

#11

print("")
print("11 harjutus")
year=input("Kirjutage sünniaasta ")
while year.isdigit()==False:
    year=input("Kirjutage õige sünniaasta ")
if ((2022-int(year))%5)==0:
    print("Teil on aastapäev!")
else: 
    print("Teil ei ole aastapäev")

print("Midagi on vale")

#12

print("")
print("12 harjutus")
hindE=input("Kirjutage kauba hind (Terve tükk eurost) ")
while hindE.isdigit()==False:
    hindE=input("Kirjutage õige kauba hind (Terve tükk eurost) ")
hindC=input("Kirjutage kauba hind (Saldo sentides) ")
while hindC.isdigit()==False:
    hindC=input("Kirjutage õige kauba hind (Saldo sentides) ")
hind=float(hindE)+float(hindC)/100
if hind>0 and hind<=10:
    summ=hind - (hind*10)/100
    print(f"Toote hind on {summ}")
elif hind>10:
    summ=hind - (hind*20)/100
    print(f"Toote hind on {summ}")
else:
    print("Üksus ei tohi olla väiksem kui null")

print("Midagi on vale")

#13

print("")
print("13 harjutus")
sugu=input("Kas te olete mees või naine?").lower()
while sugu not in ["mees","naine"]:
    sugu=input("Kirjuta õige sugu! ").lower()
if sugu=="mees":
    age=input("Kui vana sa oled?")
    while age.isdigit()==False or int(age)<=0:
        age=input("Kirjuta õige vanus! ")
    if int(age)>=16 and int(age)<=18:
        print("Sa sobid meile!")
    else:
        print("Sa ei sobi meile")
else:
    print("Sa ei sobi meile!")

print("Midagi on vale")