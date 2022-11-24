laud = ''
global tagasi3
tagasi3 = []

def kasutaja_laud(lauad):

    i = 0
    mat_laud = lauad[0].split('\n')
    mat_laud.pop(0) #võtab numbritega päiserea ära
    mat_laud.pop(0) #võtab kriipsudega päiserea ära
    puhas_laud = []
    
    #võtab laualt ära tähed A,B jne
    for rida in mat_laud:
        uus_rida = rida.replace(chr(65 + i), '')
        puhas_laud.append(uus_rida)
        i += 1
    puhtam_laud = []
    
    #võtab laualt ära ääred ehk "|"
    for rida in puhas_laud:
        uuem_rida = rida.replace('|', '').strip()
        puhtam_laud.append(uuem_rida)
    global indeks_laud
    indeks_laud = []
    
    #laud, kus on ainult sidekriipsud "-"
    for rida in puhtam_laud:
        asukohad = rida.split(' ') #asukohtadeks on sidekriipsud "-"
        indeks_laud.append(asukohad) 
    laevad_lauale()

    #paneb laua kokku ilma päise ja äärteta
    tagasi1=[]
    for rida in indeks_laud:
        tagasi1.append(''.join(rida))

    tagasi2 = []
    for rida in tagasi1:
        tagasi2.append(''.join(rida))
    for rida in tagasi2:
        tagasi3.append(' '.join(rida))
    tagasi3.pop()
    muudetud_laud()




def algne_laud(laud):
    global päis
    päis = '    0 1 2 3 4 5 6 7 8 9\n  +---------------------+\n'
    number = 0
    
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
    mangija_laud = algne_laud(laud)
    print(mangija_laud)
    print('\n ARVUTI LAUD')
    arvuti_laud = algne_laud(laud)
    print(arvuti_laud)
    global lauad
    lauad = [mangija_laud, arvuti_laud]
    kasutaja_laud(lauad)

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
        konverter(x)
    for x in laevad2k:
        konverter(x)
    for x in laevad3k:
        konverter(x)
    for x in laevad4k:
        konverter(x)




    

def laevad(laev, laevade_arv, laeva_pikkus):
    t = True
    for x in range(0, laevade_arv):
        kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
        pikkus = kordinaadid.split()
        for y in pikkus:
            if len(y) != 2:
                t = False
                break
            elif y[0].isalpha() == False or y[1].isnumeric () == False:
                t = False
                break
        while True:
            if len(pikkus) != laeva_pikkus:
                print('Sisestus ebatäpne, proovi uuesti.')  
                kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break
            elif t == False:
                print('Sisestus ebatäpne, proovi uuesti.')  
                kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break
            elif konverter(kordinaadid) == 'koht on juba võetud':
                print('Koht on juba võetud')
                kordinaadid = input('Sisesta ' + str(x+1) +'. ' + str(laeva_pikkus) + '-kohalise laeva kordinaadid: ').upper()
                pikkus = kordinaadid.split()
                t = True
                for y in pikkus:
                    if len(y) != 2:
                        t = False
                        break
            else:
                laev.append(kordinaadid)
                break  
  

#paneb nt A2 A3 jms järgi laeva lauale
def konverter(muudetav): #muudetav on nt A2 A3
    lst = muudetav.split(' ')
    for koordinaat in lst:      
        x_telg = int(ord(koordinaat[0])) - 65 #teeb tähe numbriks
        y_telg = int(koordinaat[1])
        if indeks_laud[x_telg][y_telg] != 'L':
            indeks_laud[x_telg][y_telg] = "L"
        else:
            return "koht on juba võetud"
        
    return "konverditud"
        
    
def muudetud_laud():
    g = 0
    print(päis.strip('\n'))
    for rida in tagasi3:
        print(chr(65 + g) + '| ' + rida + ' |')
        g += 1
    uus_alus = ' ' + alus.strip()
    print(uus_alus)
    

            

tosi = True
while tosi:

    kusimus = input('Kas oled valmis mängima? Y/N ')
    if kusimus == 'N' or kusimus == 'n':
        print('Mäng läbi')
        tosi = False
    elif kusimus == 'Y' or kusimus == 'y':
        prindi_laud()
        tosi = False
    else:
        print('Ei saanud sisestusest aru, palun proovi uuesti.')

