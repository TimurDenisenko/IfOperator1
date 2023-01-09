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
kp1=input("Ristkülikukujulise põranda esimese külje pikkus - ").replace(",",".",1)
while kp1.replace(".","",1).isdigit()==False or float(kp1)==0:
    print("Palun kirjuta õige number")
    kp1=input("Ristkülikukujulise põranda esimese külje pikkus - ").replace(",",".",1)
kp2=input("Ristkülikukujulise põranda teiseks külje pikkus - ").replace(",",".",1)
while kp2.replace(".","",1).isdigit()==False or float(kp2)==0:
    print("Palun kirjuta õige number")
    kp2=input("Ristkülikukujulise põranda teiseks külje pikkus - ").replace(",",".",1)
kp1=float(kp1)
kp2=float(kp2)
S=kp1 * kp2
print(f"Teie põrandapind - {S}")
remont=input("Kas soovite põrandat renoveerida? (jah või ei) ").lower()
while remont not in ["jah","ei"]:
    remont=input("Palun kirjuta jah või ei - ").lower().replace(",",".",1)
if remont=="jah":
    hind=input("Kui palju maksab üks ruutmeeter eurodes? ")
    while hind.replace(".","",1).isdigit()==False or float(hind)==0:
        hind=input("Kirjuta õige hindes ").replace(",",".",1)
    hind=float(hind)
    hindS = hind * S
    print(f"Remondi hind - {hindS} euro")
else:
    print("Kahju, tulge kui soovite remonti teha!")

#4
print("")
print("4 Harjutus")
hind = input("Palju ese maksab? ").replace(",",".",1)
while hind.replace(".","",1).isdigit()==False or float(hind)==0:
    hind=input("Kirjuta õige hind! ").replace(",",".",1)
hind=float(hind)
if hind>700 :
    hindP= (hind * 30)/100
    print(f"Sinu allahindlust on {hindP}")
else:
    print("Sulle allahindlust ei tehta!")

#5
print("")
print("5 Harjutus")
grad=input("Mis on temperatuur majas? ").replace(",",".",1)
while grad.replace(".","",1).replace("-","",1).isdigit()==False :
    grad=input("Kirjuta õige temperatuur! ").replace(",",".",1)
grad=float(grad)
if grad>=18:
    print("Suurepärane temperatuur!")
else:
    print("Lülitage patareid sisse!")

#6
print("")
print("6 Harjutus")
pikkus=input("Kui pikkus sa oled? ").replace(",",".",1)
while pikkus.replace(".","",1).isdigit()==False or int(pikkus)!=float(pikkus) or float(pikkus)<70 or float(pikkus)>250:
    pikkus=input("Kirjuta õige pikkus! ").replace(",",".",1)
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
pikkus=input("Kui pikkus sa oled? ").replace(",",".",1)
while pikkus.replace(".","",1).isdigit()==False or int(pikkus)!=float(pikkus) or float(pikkus)<70 or float(pikkus)>250:
    pikkus=input("Kirjuta õige pikkus! ").replace(",",".",1)
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

#8
print("")
print("8 Harjutus")
piima=input("Kas sa tahad osta piima? (jah või ei) ").lower()
while piima not in ["jah", "ei"]:
    piima=input("Kirjuta ainult jah või ei! ").lower()
if piima=="jah":
    hindPiima=input("Kui palju maksab piima? ").replace(",",".",1)
    while hindPiima.replace(".","",1).isdigit==False or float(hindPiima)==0:
        hindPiima=input("Kirjutage õige hind! ").replace(",",".",1)
    kogusPiima=input("Kui palju sa tahad osta? ")
    while kogusPiima.isdigit()==False or int(kogusPiima)==0:
        kogusPiima=input("Kirjuta õige arv! ")
else:
    hindPiima=kogusPiima=0
sai=input("Kas sa tahad osta sai (jah või ei) ").lower()
while sai not in ["jah", "ei"]:
    sai=input("Kirjuta ainult jah või ei! ").lower()
if sai=="jah":
    hindSai=input("Kui palju maksab Sai? ").replace(",",".",1)
    while hindSai.replace(".","",1).isdigit==False or float(hindSai)==0:
        hindSai=input("Kirjutage õige hind! ").replace(",",".",1)
    kogusSai=input("Kui palju sa tahad osta? ")
    while kogusSai.isdigit()==False or int(kogusSai)==0:
        kogusSai=input("Kirjuta õige arv! ")
else:
    hindSai=kogusSai=0
leib=input("Kas sa tahad osta leib (jah või ei) ").lower()
while leib not in ["jah", "ei"]:
    leib=input("Kirjuta ainult jah või ei! ").lower()
if leib=="jah":
    hindLeib=input("Kui palju maksab Leib? ").replace(",",".",1)
    while hindLeib.replace(".","",1).isdigit==False or float(hindLeib)==0:
        hindLeib=input("Kirjutage õige hind! ").replace(",",".",1)
    kogusLeib=input("Kui palju sa tahad osta? ")
    while kogusLeib.isdigit()==False or int(kogusLeib)==0:
        kogusLeib=input("Kirjuta õige arv! ")
else:
    hindLeib=kogusLeib=0
OS=float(hindPiima)*float(kogusPiima)+float(hindSai)*float(kogusSai)+float(hindLeib)*float(kogusLeib)
print(f"Ostude summa on {OS}")

#9
print("")
print("9 harjutus")
a=input("Kirjutage 1 külje pikkus - ").replace(",",".",1)
while a.replace(".","",1).isdigit()==False or float(a)==0:
    a=input("Kirjuta õige pikkus ").replace(",",".",1)
b=input("Kirjutage 2 külje pikkus - ").replace(",",".",1)
while b.replace(".","",1).isdigit()==False or float(b)==0:
    b=input("Kirjuta õige pikkus ").replace(",",".",1)
if a==b:
    print("See on ruut!")
else:
    print("See ei ole ruut!")

#10
print("")
print("10 harjutus")
a=input("Kirjutage esimene number ").replace(",",".",1)
while a.replace(".","",1).isdigit()==False:
    a=input("Kirjutage õige number ").replace(",",".",1)
b=input("Kirjutage teine number ").replace(",",".",1)
while b.replace(".","",1).isdigit()==False:
    b=input("Kirjuta õige number ").replace(",",".",1)
a=float(a)
b=float(b)
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
    if b!=0:
        t=a/b
        print(f"Tegevuse tulemus on {t}")
    else:
        print("Nulliga jagada ei saa.")

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

#12
print("")
print("12 harjutus")
hind=input("Kirjutage kauba hind ").replace(",",".",1)
while hind.replace(".","",1).isdigit()==False or float(hind)==0:
    hind=input("Kirjutage õige kauba hind ").replace(",",".",1)
if hind<=10:
    summ=hind - (hind*10)/100
    print(f"Toote hind on {summ}")
else:
    summ=hind - (hind*20)/100
    print(f"Toote hind on {summ}")

#13
print("")
print("13 harjutus")
sugu=input("Kas te olete mees või naine?").lower()
while sugu not in ["mees","naine"]:
    sugu=input("Kirjuta õige sugu! ").lower()
if sugu=="mees":
    age=input("Kui vana sa oled?")
    while age.isdigit()==False or int(age)==0:
        age=input("Kirjuta õige vanus! ")
    if int(age)>=16 and int(age)<=18:
        print("Sa sobid meile!")
    else:
        print("Sa ei sobi meile")
else:
    print("Sa ei sobi meile!")