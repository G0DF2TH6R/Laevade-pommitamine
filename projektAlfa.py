from random import *

# alguses pole laevu kummalgi laual
vastaslaud = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                   '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                   '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                   '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]
kasutaja_laud = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                      '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                      '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                      '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                 ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]

vastaslaud_mulle = [['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                   '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                   '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-',
                                                                   '-', '-', '-', '-', '-', '-', '-', '-', '-'],
              ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-']]


# tehakse tühi laud


def algne_laud():
    global päis
    päis = '    0 1 2 3 4 5 6 7 8 9\n  +---------------------+\n'
    number = 0
    laud = ''

    # paneb tähed vasakule paika
    for x in range(10):
        laud += chr(65 + number) + ' |' + 10 * ' -' + ' |' + '\n'
        number += 1

    laud = laud.strip()
    global alus
    alus = '\n  +---------------------+'
    return päis + laud + alus


def prindi_laud():
    print("\nREEGLID: \n1. Sisesta oma laevad (1 neljakohaline, 2 kolmekohalist, 3 kahekohalist, 4 ühekohalist)\n" +
          "2. Sina ja arvuti hakkate kordamööda pommitama üksteise laevu.\n" +
          "Kui kumbki saab teisele pihta, on võimalik uuesti tulistada\n" +
          "3. Sümbolid: - - tühi koht, X - pihta saanud laevaosa, O - Mööda lastud koht, L - Sinu laeva asukohad\n" +
          "4. Kaotab see, kellel on kõik laevad uppunud.\n")
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


# Küsib laeva koordinaate, kontrollib neid ja paneb kasutaja lauale


def laevad(laev, laevade_arv, laeva_pikkus):
    t = True
    for x in range(0, laevade_arv):
        kordinaadid = input('Sisesta ' + str(x+1) + '. ' +
                            str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
        # hakkab kontrollima, kas oli õigesti sisestatud järjendi abil
        pikkus = kordinaadid.split()
        for y in pikkus:
            # igal järjendi elemendil y (nt A1) peab olema pikkus 2
            if len(y) != 2:
                t = False
                # viib järgmisesse while True tsüklisse
                break
            elif y[0].isalpha() == False or y[1].isnumeric() == False:
                t = False
                break

        # kontrollitakse veel sisestatu õigsust
        while True:
            # vaadatakse antud sõne pikkust
            if len(pikkus) != laeva_pikkus:
                print('Sisestus ebatäpne, proovi uuesti.')
                kordinaadid = input('Sisesta ' + str(x+1) + '. ' +
                                    str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break

            # kui kusagil muutus t Falseiks vale sisestuse tõttu, siis küsitakse uuesti sisestust
            elif t == False:
                print('Sisestus ebatäpne, proovi uuesti.')
                kordinaadid = input('Sisesta ' + str(x+1) + '. ' +
                                    str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break

            # minnakse laevu laua peale panema + selle kontroll
            elif konverter(kordinaadid, kasutaja_laud) == 'koht on juba võetud':
                print('Koht on juba võetud')
                kordinaadid = input('Sisesta ' + str(x+1) + '. ' +
                                    str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break
            else:
                # paneb laevad4k järjendisse A2 jne listi
                laev.append(kordinaadid)

                global kasutaja_laeva_indeks
                # Kasutaja laeva indeks sõnaraamatusse kasutaja_mapp,
                # tekkide arv listi kasutaja_laev
                lisada_kasutaja_mappi(
                    kordinaadid, kasutaja_laeva_indeks, laeva_pikkus)
                kasutaja_laeva_indeks += 1
                break

        print(muudetud_laud(kasutaja_laud))


# paneb nt A2 A3 jms järgi laeva lauale
def konverter(muudetav, muudetav_laud):  # muudetav on nt A2 A3
    lst = muudetav.strip().split(' ')
    for koordinaat in lst:
        x_telg = int(ord(koordinaat[0])) - 65  # teeb tähe numbriks
        y_telg = int(koordinaat[1])
        if muudetav_laud[x_telg][y_telg] == 'L':
            return "koht on juba võetud"
    for koordinaat in lst:
        x_telg = int(ord(koordinaat[0])) - 65  # mitmes järjend kasutaja_lauas
        y_telg = int(koordinaat[1])

        # leiab koordinaadi asukoha laual ja paneb sinna laeva
        # y-telg näitab mitmes kriips reas
        muudetav_laud[x_telg][y_telg] = 'L'

    return "konverditud"

# paneb juurde uuele kasutaja_lauale päise ja aluse ning joondab õigesti


def muudetud_laud(laud):
    # g abil saab tähed kokku panna
    g = 0
    print(päis.strip('\n'))
    for rida in laud:
        print(chr(65 + g) + ' | ' + ' '.join(rida) + ' |')
        g += 1
    uus_alus = '  ' + alus.strip()
    print(uus_alus)


def arvuti_laud():
    x = 10
    while x > 0:
        # teeb ühe neljakohalise
        if x > 9:
            kordinaadid = ''
            laeva_asukoht_xtelg = str(randint(0, 5))  # 6ni, sest 6+4 > 9
            laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
            for y in range(4):
                kordinaadid += laeva_asukoht_ytelg + \
                    str((int(laeva_asukoht_xtelg) + y)) + ' '
            # indeks 0 sõnaraamatusse koordinaatide järgi ja 4 tekki
            lisada_arvuti_mappi(kordinaadid, 0, 4)  # Lisatud
            konverter(kordinaadid, vastaslaud)
        # siia jõutakse 2 korda, seega tehakse kaks 3-kohalist
        elif x > 7:
            while True:
                kordinaadid = ""
                laeva_asukoht_xtelg = str(randint(0, 6))
                laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
                for y in range(3):
                    kordinaadid += laeva_asukoht_ytelg + \
                        str((int(laeva_asukoht_xtelg) + y)) + ' '
                if konverter(kordinaadid, vastaslaud) == "konverditud":
                    # indeksid 1, 2 sõnaraamatusse koordinaatide järgi ja 3 tekki
                    lisada_arvuti_mappi(kordinaadid, x-7, 3)  # Lisatud
                    break
        #kahelised
        elif x > 4:
            while True:
                kordinaadid = ""
                laeva_asukoht_xtelg = str(randint(0, 7))
                laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
                for y in range(2):
                    kordinaadid += laeva_asukoht_ytelg + \
                        str((int(laeva_asukoht_xtelg) + y)) + ' '
                if konverter(kordinaadid, vastaslaud) == "konverditud":
                    # indeksid 3, 4, 5 sõnaraamatusse koordinaatide järgi ja 2 tekki
                    lisada_arvuti_mappi(kordinaadid, x-2, 2)  # Lisatud
                    break

        # ühelisi tehakse x=4st kuni x=1ni (4 korda)
        else:
            while True:
                kordinaadid = ""
                laeva_asukoht_xtelg = str(randint(0, 9))
                laeva_asukoht_ytelg = choice('ABCDEFGHIJ')
                for y in range(1):
                    kordinaadid += laeva_asukoht_ytelg + \
                        str((int(laeva_asukoht_xtelg) + y)) + ' '
                if konverter(kordinaadid, vastaslaud) == "konverditud":
                    # indeksid 6 7 8 9 sõnaraamatusse koordinaatide järgi ja 1 tekki
                    lisada_arvuti_mappi(kordinaadid, x+5, 1)  # Lisatud
                    toene = False
                    break

        x -= 1

    return muudetud_laud(vastaslaud)

# -------------------------------------------------------------------


kasutaja_laevade_arv = 10

arvuti_laevade_arv = 10

kasutaja_tuli = "" #koordinaatides

kasutaja_seis = "Möödas"

arvuti_seis = "Möödas"

# Arvuti tulistatud koordinaatide kogum
vetoSet_arvuti = []

# Kasutaja laevade sõnastik koordinaat -> indeks ehk järjekorra nr
kasutaja_mapp = {}
kasutaja_laeva_indeks = 0
# Kasutaja laevade indeks -> tekkide arv
kasutaja_laev = []
# Arvuti laevade sõnastik koordinaat -> indeks
arvuti_mapp = {}
# Arvuti laevade indeks -> tekkide arv
arvuti_laev = []

def on_kasutaja_elus():
    return kasutaja_laevade_arv > 0


def on_arvuti_elus():
    return arvuti_laevade_arv > 0

# Paneb laeva koordinaadid sõnastikku indeksiga kasutaja_mapp ja
# lisab tekkide(mitme kohaline laev) arvu listi kasutaja_laev


def lisada_kasutaja_mappi(koordinaadid, indeks, tekkide_arv):
    loend = koordinaadid.strip().split(' ')
    for kooordinaat in loend:
        kasutaja_mapp[kooordinaat] = indeks
    kasutaja_laev.append(tekkide_arv)

# Paneb laeva koordinaadid sõnastikku indeksiga arvuti_mapp ja
# lisab tekkide arvu listi arvuti_laev


def lisada_arvuti_mappi(koordinaadid, indeks, tekkide_arv):
    loend = koordinaadid.strip().split(' ')
    for kooordinaat in loend:
        #indeks on laeva järjekorra nr
        arvuti_mapp[kooordinaat] = indeks
    arvuti_laev.append(tekkide_arv)


def märk_lauale(laud, tuli, märk):
    x_telg = int(ord(tuli[0])) - 65  # mitmes järjend kasutaja_lauas
    y_telg = int(tuli[1])

    laud[x_telg][y_telg] = märk


def märk_laualt(laud, tuli):
    x_telg = int(ord(tuli[0])) - 65
    y_telg = int(tuli[1])
    return laud[x_telg][y_telg]


# 1. Kasutaja annab tuld

def kasutaja_tuld():
    while True:
        koordinaat = input("Sisesta tule koordinaat: ").upper()
        if len(koordinaat) != 2:
            continue
        if koordinaat[0].isalpha() == False or koordinaat[1].isnumeric() == False:
            continue
        if koordinaat[0] > 'J':
            continue
        break
    global kasutaja_tuli
    kasutaja_tuli = koordinaat
    return koordinaat

# 2. Vaatame kas tulistamine läheb laeva pihta


def kasutaja_tule_vastuvõtt(tuli):
    global arvuti_laevade_arv
    global arvuti_seis
    if märk_laualt(vastaslaud, tuli) == 'L':
        print("\n*** On tabamus! ***")
        arvuti_seis = "Tabamus"
        
        #vajame indeksit selleks, et teada kas laev on täielikult põhjas
        
        indeks = arvuti_mapp[tuli]  # saame laeva indeksi sõnastikust võetud koordinaadi abil
        # üks osa laevast on hävitatud
        # jrj-s olevate tekkide arvu vähendamine
        arvuti_laev[indeks] -= 1
        
        # jrj-i indeks==indeks sõnastikust ja talle vastab järjendis tema tekkide arv
        if arvuti_laev[indeks] == 0:
            arvuti_seis = "Põhjas"
            print("Arvuti laev hävitatud  !!!")
            arvuti_laevade_arv -= 1
    else:
        arvuti_seis = "Möödas"
        print("\n*** Mööda ***")
    print('\n')

# 3. Kasutaja tule analüüs arvuti poolt

# kasutaja_tule_vastuvõtus() sai arvuti_seis mingi oleku
# selle järgi pannakse lauale vastavale koordinaadile vastav märk 


def arvuti_tule_seis():
    # arvuti_seis - arvuti teatamine kasutaja tule tulemusest

    if arvuti_seis == "Möödas":
        märk_lauale(vastaslaud_mulle, kasutaja_tuli, 'O')
    elif arvuti_seis == "Tabamus":
        märk_lauale(vastaslaud_mulle, kasutaja_tuli, 'X')
    elif arvuti_seis == "Põhjas":
        märk_lauale(vastaslaud_mulle, kasutaja_tuli, 'X')
        
# 4. Arvuti pommitab


def arvuti_tuld():
    global arvuti_tuli
    arvuti_tuli = ""
    while True:
        x = choice('ABCDEFGHIJ')
        y = str(randint(0, 9))
        arvuti_tuli = x + y
        # vetoSetis on koordinaadid, mida on juba kasutatud
        # kontrollib, et varem poleks kasutatud neid koordinaate
        if vetoSet_arvuti.count(arvuti_tuli) == 0:
            break
    vetoSet_arvuti.append(arvuti_tuli)

# Vaatame, kas kasutaja saab pihta ja seame oleku


def arvuti_tule_vastuvõtt(tuli):
    print("Arvuti lask: " + tuli + '\n')
    global kasutaja_seis
    global kasutaja_laevade_arv
    if märk_laualt(kasutaja_laud, tuli) == 'L':
        print("*** On tabamus ***")
        märk_lauale(kasutaja_laud, tuli, 'X')
        kasutaja_seis = "Tabamus"
        
        indeks = kasutaja_mapp[tuli]  # Laeva indeks koordinaadi tuli järgi
        kasutaja_laev[indeks] -= 1
        
        if kasutaja_laev[indeks] == 0:
            kasutaja_seis = "Põhjas"
            print("Oh õudust, põhjas!")
            kasutaja_laevade_arv -= 1
    else:
        kasutaja_seis = "Möödas"
        print("*** Mööda! ***")
        märk_lauale(kasutaja_laud, tuli, 'O')
    print('\n')

# -------------------------------------------------------------------


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

        # Mängu põhiline ring
        while on_kasutaja_elus() and on_arvuti_elus():
            # kui kasutaja on saanud pihta või uppunud
            if kasutaja_seis != "Möödas":
                print("Jääb vahele...: <Enter>")
                input()
            else:
                kasutaja_tuld()
                kasutaja_tule_vastuvõtt(kasutaja_tuli)
                arvuti_tule_seis()
                if not on_arvuti_elus():
                    muudetud_laud(kasutaja_laud)
                    muudetud_laud(vastaslaud)
                    break
                
            if arvuti_seis != "Möödas":
                print("\nArvuti lask: Jääb vahele...\n")
            else:
                arvuti_tuld()
                arvuti_tule_vastuvõtt(arvuti_tuli)
            muudetud_laud(kasutaja_laud)
            muudetud_laud(vastaslaud_mulle)
        if on_kasutaja_elus():
            print("\n:-))) Hurraa! Võit!!! :-)))\n")
        else:
            print("\n:-((( Kahju. Vastane osutus tugevamaks\n")
        print("Mäng läbi, vajuta <Enter>")
        input()

    else:
        print('Ei saanud sisestusest aru, palun proovi uuesti.')

