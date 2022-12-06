from random import *

vastaslaud = [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]
kasutaja_laud = [['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-'],
['-','-','-','-','-','-','-','-','-','-'],['-','-','-','-','-','-','-','-','-','-']]





#tehakse tühi laud
def algne_laud():
    global päis
    päis = '    0 1 2 3 4 5 6 7 8 9\n  +---------------------+\n'
    number = 0
    laud = ''
    
    #paneb tähed vasakule paika
    for x in range(10):
        laud += chr(65 + number) + ' |' + 10 * ' -' + ' |' +'\n'
        number += 1
    
    laud = laud.strip()
    global alus
    alus = '\n  +---------------------+'
    return päis + laud + alus


def prindi_laud():
    print("\nREEGLID: \n 1. Sisesta oma laevad (1 neljakohaline, 2 kolmekohalist, 3 kahekohalist)\n"+
    "2. Sina ja arvuti hakkate kordamööda pommitama üksteise laevu.\n"+
    "Kui kumbki saab teisele pihta, on võimalik uuesti tulistada\n"+
    "3. Sümbolid: - - tühi koht, X - pihta saanud laevaosa, O - Mööda lastud koht, L - Sinu laeva asukohad\n"+
    "4. Kaotab see kellel on kõik laevad uppunud.\n")
    print('SINU LAUD')
    print(algne_laud())
    print('\n ARVUTI LAUD')
    print(algne_laud())

def laevad_lauale():

    laevad1k = []
    laevad2k = []
    laevad3k = []
    laevad4k = []
    laevad(laevad4k, 1, 4)
    laevad(laevad3k, 2, 3)
    laevad(laevad2k, 3, 2)
    laevad(laevad1k, 4, 1)
    for x in laevad1k:
        konverter(x, kasutaja_laud)
    for x in laevad2k:
        konverter(x, kasutaja_laud)
    for x in laevad3k:
        konverter(x, kasutaja_laud)
    for x in laevad4k:
        konverter(x, kasutaja_laud)




    
#Küsib laeva koordinaate, kontrollib neid ja paneb kasutaja lauale
def laevad(laev, laevade_arv, laeva_pikkus):
    t = True
    for x in range(0, laevade_arv):
        kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
        #hakkab kontrollima, kas oli õigesti sisestatud järjendi abil
        pikkus = kordinaadid.split()
        for y in pikkus:
            #igal järjendi elemendil y (nt A1) peab olema pikkus 2
            if len(y) != 2:
                t = False
                #viib järgmisesse while True tsüklisse
                break
            elif y[0].isalpha() == False or y[1].isnumeric () == False:
                t = False
                break
            
        #kontrollitakse veel sisestatu õigsust
        while True:
            #vaadatakse antud sõne pikkust
            if len(pikkus) != laeva_pikkus:
                print('Sisestus ebatäpne, proovi uuesti.')  
                kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break
                    
            #kui kusagil muutus t Falseiks vale sisestuse tõttu, siis küsitakse uuesti sisestust
            elif t == False:
                print('Sisestus ebatäpne, proovi uuesti.')  
                kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break
                    
            #minnakse laevu laua peale panema + selle kontroll
            elif konverter(kordinaadid, kasutaja_laud) == 'koht on juba võetud':
                print('Koht on juba võetud')
                kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break
            else:
                #paneb laevad4k järjendisse A2 jne listi
                laev.append(kordinaadid)
                break
        
        print(muudetud_laud(kasutaja_laud))
  

#paneb nt A2 A3 jms järgi laeva lauale
def konverter(muudetav, muudetav_laud): #muudetav on nt A2 A3
    lst = muudetav.split(' ')
    for koordinaat in lst:      
        x_telg = int(ord(koordinaat[0])) - 65 #teeb tähe numbriks
        y_telg = int(koordinaat[1])
        if muudetav_laud[x_telg][y_telg] == 'L':
            return "koht on juba võetud"
    for koordinaat in lst:      
        x_telg = int(ord(koordinaat[0])) - 65 
        y_telg = int(koordinaat[1])
        #leiab koordinaadi asukoha laual ja paneb sinna laeva
        muudetav_laud[x_telg][y_telg] = 'L'
        
    return "konverditud"
        
# võtab kasutaja_laua, millel on nüüd mingikohalised laevad
# pannakse kokku valmis laud
def muudetud_laud(laud):
    # g abil saab tähed kokku panna
    g = 0
    print(päis.strip('\n'))
    for rida in laud:
        print(chr(65 + g) + ' | ' + ' '.join(rida) + ' |')
        g += 1
    uus_alus = '  ' + alus.strip()
    print(uus_alus)

def ai_laud():
    x = 10
    while x > 0:
        if x > 9:
            kordinaadid = ''
            laeva_asukoht_xtelg = str(randint(0,6))
            laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
            for y in range(4):
                kordinaadid += laeva_asukoht_ytelg + str(int(laeva_asukoht_xtelg + y)) + ' '
            konverter(kordinaadid, vastaslaud)
        elif x > 7:
            kordinaadid = ''
            laeva_asukoht_xtelg = str(randint(0,7))
            laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
            for y in range(3):
                kordinaadid += laeva_asukoht_ytelg + str(int(laeva_asukoht_xtelg + y)) + ' '
            while True:
                if konverter(kordinaadid, vastaslaud) == 'konverditud':
                    break
                else:
                    konverter(kordinaadid, vastaslaud)
        elif x > 4:
            kordinaadid = ''
            laeva_asukoht_xtelg = str(randint(0,8))
            laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
            for y in range(2):
                kordinaadid += laeva_asukoht_ytelg + str(int(laeva_asukoht_xtelg + y)) + ' '
            konverter(kordinaadid, vastaslaud)
            while True:
                if konverter(kordinaadid, vastaslaud) == 'konverditud':
                    break
                else:
                    konverter(kordinaadid, vastaslaud)
        else:
            kordinaadid = ''
            laeva_asukoht_xtelg = str(randint(0,10))
            laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
            for y in range(1):
                kordinaadid += laeva_asukoht_ytelg + str(int(laeva_asukoht_xtelg + y)) + ' '
            konverter(kordinaadid, vastaslaud)
            while True:
                if konverter(kordinaadid, vastaslaud) == 'konverditud':
                    break
                else:
                    konverter(kordinaadid, vastaslaud)
        x -= 1


        
            

tosi = True
while tosi:

    kusimus = input('Kas oled valmis mängima? Y/N ')
    if kusimus == 'N' or kusimus == 'n':
        print('Mäng läbi')
        tosi = False
    elif kusimus == 'Y' or kusimus == 'y':
        prindi_laud()
        tosi = False
        laevad_lauale()
        muudetud_laud(kasutaja_laud)
        laevad_lauale()
        muudetud_laud(kasutaja_laud)
    else:
        print('Ei saanud sisestusest aru, palun proovi uuesti.')




