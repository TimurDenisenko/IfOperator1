from math import *
#1
try:
    print("1 Harjutus")
    nimi = input("Mis sinu nimi on? ")
    if nimi.lower() == "juku":
        print("Läheme kinno!")
        age = int(input("Kui vana sa oled? "))
        if age<6 and age>0 :
            print("Sinu pilet on tasuta")
        elif age>=6 and age<14:
            print("Sinu pilet on lastpilet")
        elif age>=15 and age<=65:
            print("Sinu pilet on täispilet")
        elif age>65 and age<100:    
            print("Sinu pilet on sooduspilet")
        elif age<=0 or age>=100:
            print("Viga andmetega")
    else:
        print("Ilus nimi")
except:
    print("Midagi on vale")

#2
try:
    print("")
    print("2 Harjutus")
    naber1=input("1 inimene, mis sinu nimi on? ")
    naber2=input("2 inimene, mis sinu nimi on? ")
    if naber1.isalpha()==True and naber2.isalpha()==True:
        if naber1.lower()=="timur" and naber2.lower()=="juku":
            print(f"{naber1} ja {naber2} te olete nüüd naabrid")
        else:
            print("Head nimed!")
    else:
        print("Palun kirjuta õige nimi!")
except:
    print("Midagi on vale")

#3
try:
    print("")
    print("3 Harjutus")
    kp1=float(input("Ristkülikukujulise põranda esimese külje pikkus - "))
    kp2=float(input("Ristkülikukujulise põranda teiseks külje pikkus - "))
    if kp1>0 and kp2>0:
        S=kp1 * kp2
        print(f"Teie põrandapind - {S}")
        remont=input("Kas soovite põrandat renoveerida? (ja või ei) ")
        if remont=="ja":
           hind=float(input("Kui palju maksab üks ruutmeeter eurodes? "))
           if hind>0:
             hindS = hind * S
             print(f"Remondi hind - {hindS} euro")
           elif remont=="ei":
                print("Kahju, tulge kui soovite remonti teha!")
    else:
        print("Kirjuta õige number")
except:
    print("Midagi on vale")

#4
try:
    print("")
    print("4 Harjutus")
    hind = float(input("Palju ese maksab? "))
    if hind>700 :
        hindP= (hind * 30)/100
        print(f"Sinu allahindlust on {hindP}")
    else:
        print("Sulle allahindlust ei tehta!")
except:
    print("Midagi on vale")

#5
try:
    print("")
    print("5 Harjutus")
    grad=float(input("Mis on temperatuur majas? "))
    if grad>=18:
        print("Suurepärane temperatuur!")
    elif grad<18:
        print("Lülitage patareid sisse!")
    else:
        print("Palun kirjuta õige temperatuur!")
except:
    print("Midagi on vale")

#6
try:
    print("")
    print("6 Harjutus")
    pikkus=float(input("Kui pikkus sa oled? "))
    if pikkus<=150 and pikkus>=70:
        print("Sa oled lühike")
    elif pikkus>150 and pikkus<=180:
        print("Sa oled keskmine")
    elif pikkus>180 and pikkus<250:
        print("Sa oled pikk")
    else:
        print("Palun kirjuta õige pikkus!")
except:
    print("Midagi on vale")

#7
try:
    print("")
    print("7 Harjutus")
    sugu=input("Kas sa oled mees või naine? ")
    pikkus=float(input("Kui pikkus sa oled? "))
    if sugu=="mees":
        if pikkus>=70 and pikkus<165:
            print("Sa oled lühike mees")
        elif pikkus>=165 and pikkus<185:
            print("Sa oled keskmine mees")
        elif pikkus>=185 and pikkus<250:
            print("Sa oled pikk mees")
        else:
            print("Palun kirjuta õige pikkus või vana!")
    elif sugu=="naine":
        if pikkus>=70 and pikkus<150:
            print("Sa oled lühike naine")
        if pikkus>=150 and pikkus<170:
            print("Sa oled keskmine naine")
        if pikkus>=170 and pikkus<250:
            print("Sa oled pikk naine")
        else:
            print("Palun kirjuta õige pikkus või vana!")
    else:
        print("Palun kirjuta õige sugu!")
except:
    print("Midagi on vale")

#8
try:
    print("")
    print("8 Harjutus")
    piima=input("Kas sa tahad osta piima? (ja või ei) ")
    sai=input("Kas sa tahad osta sai (ja või ei) ")
    leib=input("Kas sa tahad osta leib (ja või ei) ")
    if piima=="ei" and sai=="ei" and leib=="ei":
        print("Ostude summa on 0")
    elif piima=="ei" and sai=="ei" and leib=="ja":
        hindLeib=float(input("Kui palju maksab leib? "))
        kogusLeib=int(input("Kui palju sa tahad osta? "))
        if hindLeib>0 and kogusLeib>0:
            OS=hindLeib * kogusLeib
            print(f"Ostude summa on {OS}")
        else:
            print("Palun kirjuta õige arved")
    elif piima=="ei" and sai=="ja" and leib=="ei":
        hindSai=float(input("Kui palju maksab sai? "))
        kogusSai=int(input("Kui palju sa tahad osta? "))
        if hindSai>0 and kogusSai>0 :
            OS=hindSai * kogusSai
            print(f"Ostude summa on {OS}")
        else:
            print("Palun kirjuta õige arved")
    elif piima=="ei" and sai=="ja" and leib=="ja":
        hindSai=float(input("Kui palju maksab sai? "))
        kogusSai=int(input("Kui palju sa tahad osta? "))
        hindLeib=float(input("Kui palju maksab leib? "))
        kogusLeib=int(input("Kui palju sa tahad osta? "))
        if hindSai>0 and kogusSai>0 and hindLeib>0 and kogusLeib>0:
            OS=hindSai * kogusSai + hindLeib * kogusLeib
            print(f"Ostude summa on {OS}")
        else:
            print("Palun kirjuta õige arved")
    elif piima=="ja" and sai=="ei" and leib=="ei":
        hindPiima=float(input("Kui palju maksab piima? "))
        kogusPiima=int(input("Kui palju sa tahad osta? "))
        if hindPiima>0 and kogusPiima>0:
            OS=hindPiima * kogusPiima
            print(f"Ostude summa on {OS}")
        else:
            print("Palun kirjuta õige arved")
    elif piima=="ja" and sai=="ei" and leib=="ja":
        hindPiima=float(input("Kui palju maksab piima? "))
        kogusPiima=int(input("Kui palju sa tahad osta? "))
        hindLeib=float(input("Kui palju maksab leib? "))
        kogusLeib=int(input("Kui palju sa tahad osta? "))
        if hindPiima>0 and kogusPiima>0 and hindLeib>0 and kogusLeib>0:
            OS=hindPiima * kogusPiima + hindLeib * kogusLeib
            print(f"Ostude summa on {OS}")
        else:
            print("Palun kirjuta õige arved")
    elif piima=="ja" and sai=="ja" and leib=="ei":
        hindPiima=float(input("Kui palju maksab piima? "))
        kogusPiima=int(input("Kui palju sa tahad osta? "))
        hindSai=float(input("Kui palju maksab sai? "))
        kogusSai=int(input("Kui palju sa tahad osta? "))
        if hindPiima>0 and kogusPiima>0 and hindSai>0 and kogusSai>0:
            OS=hindPiima * kogusPiima + hindSai * kogusSai
            print(f"Ostude summa on {OS}")
        else:
            print("Palun kirjuta õige arved")
    elif piima=="ja" and sai=="ja" and leib=="ja":
        hindPiima=float(input("Kui palju maksab piima? "))
        kogusPiima=int(input("Kui palju sa tahad osta? "))
        hindSai=float(input("Kui palju maksab sai? "))
        kogusSai=int(input("Kui palju sa tahad osta? "))
        hindLeib=float(input("Kui palju maksab leib? "))
        kogusLeib=int(input("Kui palju sa tahad osta? "))
        if hindPiima>0 and kogusPiima>0 and hindSai>0 and kogusSai>0 and hindLeib>0 and kogusLeib>0:
            OS=hindPiima*kogusPiima + hindSai*kogusSai + hindLeib*kogusLeib
            print(f"Ostude summa on {OS}")
        else:
            print("Palun kirjuta õige arved")
    else:
        print("Palun kirjuta ja või ei!")
except:
    print("Midagi on vale")

#9
try:
    print("")
    print("9 harjutus")
    a=float(input("Kirjutage 1 külje pikkus - "))
    b=float(input("Kirjutage 2 külje pikkus - "))
    if a>0 and b>0:
        if a==b:
            print("See on ruut!")
        else:
            print("See ei ole ruut!")
    else:
        print("Palun kirjuta õige number!")
except:
    print("Midagi on vale")

#10
try:
    print("")
    print("10 harjutus")
    arv1=float(input("Kirjutage esimene number "))
    arv2=float(input("Kirjutage teine number "))
    s=input("Kirjutage tegevuse märk (+ - * /) ")
    if s=="+":
        t=a+b 
        print(f"Tegevuse tulemus on {t}")
    elif s=="-":
        t=a-b
        print(f"Tegevuse tulemus on {t}")
    elif s=="*":
        t=a*b 
        print(f"Tegevuse tulemus on {t}")
    elif s=="/":
        if b>0 and b<0:
            t=a/b
            print(f"Tegevuse tulemus on {t}")
        else:
            print("Nulliga jagada ei saa.")
    else:
        print("Palun kirjutage õige numbrid ja õige tegevuse märk")
except:
    print("Midagi on vale")

#11
try:
    print("")
    print("11 harjutus")
    year=int(input("Kirjutage sünniaasta "))
    old=2022-year
    old1=old%5
    if old1==0:
        print("Teil on aastapäev!")
    else: 
        print("Teil ei ole aastapäev")
except:
    print("Midagi on vale")

#12
try:
    print("")
    print("12 harjutus")
    hind=float(input("Kirjutage kauba hind "))
    if hind>0 and hind<=10:
        summ=hind - (hind*10)/100
        print(f"Toote hind on {summ}")
    if hind>10:
        summ=hind - (hind*20)/100
        print(f"Toote hind on {summ}")
    else:
        print("Palun kirjutage õige hind!")
except:
    print("Midagi on vale")

#13
try:
    print("")
    print("13 harjutus")
    sugu=input("Kas te olete mees või naine?")
    if sugu=="mees":
        age=int(input("Kui vana sa oled?"))
        if age>=16 and age<=18:
            print("Sa sobid meile!")
        else:
            print("Sa ei sobi meile")
    elif sugu=="naine":
        print("Sa ei sobi meile!")
except:
    print("Midagi on vale")