from math import *
#1
try:
    print("1 Harjutus")
    nimi = input("Mis sinu nimi on? ")
    if nimi.lower() == "juku":
        print("L�heme kinno!")
        age = int(input("Kui vana sa oled? "))
        if age<6 and age>0 :
            print("Sinu pilet on tasuta")
        elif age>=6 and age<14:
            print("Sinu pilet on lastpilet")
        elif age>=15 and age<=65:
            print("Sinu pilet on t�ispilet")
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
            print(f"{naber1} ja {naber2} te olete n��d naabrid")
        else:
            print("Head nimed!")
    else:
        print("Palun kirjuta �ige nimi!")
except:
    print("Midagi on vale")

#3
try:
    print("")
    print("3 Harjutus")
    kp1=float(input("Ristk�likukujulise p�randa esimese k�lje pikkus - "))
    kp2=float(input("Ristk�likukujulise p�randa teiseks k�lje pikkus - "))
    if kp1>0 and kp2>0:
        S=kp1 * kp2
        print(f"Teie p�randapind - {S}")
        remont=input("Kas soovite p�randat renoveerida? (ja v�i ei) ")
        if remont=="ja":
           hind=float(input("Kui palju maksab �ks ruutmeeter eurodes? "))
           if hind>0:
             hindS = hind * S
             print(f"Remondi hind - {hindS} euro")
           elif remont=="ei":
                print("Kahju, tulge kui soovite remonti teha!")
    else:
        print("Kirjuta �ige number")
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
        print("Suurep�rane temperatuur!")
    elif grad<18:
        print("L�litage patareid sisse!")
    else:
        print("Palun kirjuta �ige temperatuur!")
except:
    print("Midagi on vale")

#6
try:
    print("")
    print("6 Harjutus")
    pikkus=float(input("Kui pikkus sa oled? "))
    if pikkus<=150 and pikkus>=70:
        print("Sa oled l�hike")
    elif pikkus>150 and pikkus<=180:
        print("Sa oled keskmine")
    elif pikkus>180 and pikkus<250:
        print("Sa oled pikk")
    else:
        print("Palun kirjuta �ige pikkus!")
except:
    print("Midagi on vale")

#7
try:
    print("")
    print("7 Harjutus")
    sugu=input("Kas sa oled mees v�i naine? ")
    pikkus=float(input("Kui pikkus sa oled? "))
    if sugu=="mees":
        if pikkus>=70 and pikkus<165:
            print("Sa oled l�hike mees")
        elif pikkus>=165 and pikkus<185:
            print("Sa oled keskmine mees")
        elif pikkus>=185 and pikkus<250:
            print("Sa oled pikk mees")
        else:
            print("Palun kirjuta �ige pikkus v�i vana!")
    elif sugu=="naine":
        if pikkus>=70 and pikkus<150:
            print("Sa oled l�hike naine")
        if pikkus>=150 and pikkus<170:
            print("Sa oled keskmine naine")
        if pikkus>=170 and pikkus<250:
            print("Sa oled pikk naine")
        else:
            print("Palun kirjuta �ige pikkus v�i vana!")
    else:
        print("Palun kirjuta �ige sugu!")
except:
    print("Midagi on vale")

#8
try:
    print("")
    print("8 Harjutus")
    piima=input("Kas sa tahad osta piima? (ja v�i ei) ")
    sai=input("Kas sa tahad osta sai (ja v�i ei) ")
    leib=input("Kas sa tahad osta leib (ja v�i ei) ")
    if piima=="ei" and sai=="ei" and leib=="ei":
        print("Ostude summa on 0")
    elif piima=="ei" and sai=="ei" and leib=="ja":
        hindLeib=float(input("Kui palju maksab leib?"))
        print(f"Ostude summa on {hindLeib}")
    elif piima=="ei" and sai=="ja" and leib=="ei":
        hindSai=float(input("Kui palju maksab sai?"))
        print(f"Ostude summa on {hindSai}")
    elif piima=="ei" and sai=="ja" and leib=="ja":
        hindSai=float(input("Kui palju maksab sai?"))
        hindLeib=float(input("Kui palju maksab leib?"))
        OS=hindSai + hindLeib
        print(f"Ostude summa on {OS}")
    elif piima=="ja" and sai=="ei" and leib=="ei":
        hindPiima=float(input("Kui palju maksab piima?"))
        print(f"Ostude summa on {hindPiima}")
    elif piima=="ja" and sai=="ei" and leib=="ja":
        hindPiima=float(input("Kui palju maksab piima?"))
        hindLeib=float(input("Kui palju maksab leib?"))
        OS=hindPiima + hindLeib
        print(f"Ostude summa on {OS}")
    elif piima=="ja" and sai=="ja" and leib=="ei":
        hindPiima=float(input("Kui palju maksab piima?"))
        hindSai=float(input("Kui palju maksab sai?"))
        OS=hindPiima + hindSai
        print(f"Ostude summa on {OS}")
    elif piima=="ja" and sai=="ja" and leib=="ja":
        hindPiima=float(input("Kui palju maksab piima?"))
        hindSai=float(input("Kui palju maksab sai?"))
        hindLeib=float(input("Kui palju maksab leib?"))
        OS=hindPiima+hindSai+hindLeib
        print(f"Ostude summa on {OS}")
except:
    print("Midagi on vale!!")
    print("fdsfsd")

