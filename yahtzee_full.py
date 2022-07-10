# -*- coding: cp1252 -*-
import random

wuerfel=[1,2,3,4,5] # In dieser Liste werden die Augenzahlen der Wuerfel gespeichert
reihe=0             # Variable zum anzeigen der Würfel (Reihenfolge)
runde = 1
plan=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # fuer den Spielplan
counter=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]# zum ausrechnen der Punktezahl
gesamt=0            # Gesamtpunktzahl
rundenzahl = 13

punkteOben = 0
punkteUnten = 0

fehler='Falsche Benutzereingabe'

welcheWuerfel='welche Wuerfel sollen erneut geworfen werden? / w fuer Weiter. '
erklaerung='Gib die Nummer des Würfels ein und drücke Enter. Wiederhole diesen Schritt für jeden Würfel einzeln. Gib dann w für weiter ein und Drücke Enter'

try:

    def punkte():
        global punkteOben
        global punkteUnten

        punkteOben = 0
        punkteUnten = 0

        for i in range(1, 7):
            punkteOben+=counter[i]
        for i in range(7, 14):
            punkteUnten+=counter[i]
        print ''
        print 'Punkte Oben    :', punkteOben
        if punkteOben > 63:
            print 'Bonus oben +35 :'
            punkteOben+=35
        print 'Punkte Unten   :', punkteUnten
        print 'Gesamtpunktzahl:', punkteOben+punkteUnten
        print ''

    def planZeigen():
        
        for i in range(14):
            if plan[i] == 0: plan[i] = ''

        print ''
        print '1:           1-er: ',plan[1]
        print '2:           2-er: ',plan[2]
        print '3:           3-er: ',plan[3]
        print '4:           4-er: ',plan[4]
        print '5:           5-er: ',plan[5]
        print '6:           6-er: ',plan[6]
        print '7:     3-er Pasch: ',plan[7]
        print '8:     4-er Pasch: ',plan[8]
        print '9:     Full-House: ',plan[9]
        print '10: Kleine Straße: ',plan[10]
        print '11:  Große Straße: ',plan[11]
        print '12:       Kniffel: ',plan[12]
        print '13:        Chance: ',plan[13]
        print ''

        for i in range(14):
            if plan[i] == '': plan[i] = 0


    def spielplan():
        global plan
        global wuerfel
        global counter

        counts = []
        for x in wuerfel:
            counts.append(wuerfel.count(x))
        wuerfelNeu = sorted(wuerfel)
        wuerfelNeu = list(set(wuerfelNeu))
        planZeigen()
        punkte()

        eintragen=raw_input('Wo möchtest du dein Eergebnis eintragen? / s => eine Runde Streichen. ')
        print ''
        

        if eintragen == 's':
            streichen = raw_input('Welches Feld möchtest du streichen? ')
            print ''
            plan[int(streichen)] = 'gestrichen / 0'
            counter[int(streichen)] = 0


        elif plan[int(eintragen)] == 0:

            eintragen=int(eintragen)

            if eintragen > 0 and eintragen < 7:
                gesamt=0
                gesamt=int(gesamt)
                gesamt=wuerfel.count(eintragen)*eintragen
                if gesamt != 0:
                    plan[eintragen] = gesamt
                    counter[eintragen] = gesamt
                else:
                    print 'Der Wurf enthält keine', eintragen
                    print ''
                    ask=raw_input('Null Punkte eintragen j = ja / n = nein ')
                    if ask == 'j':
                        plan[eintragen] = 'gestrichen / 0'
                        counter[eintragen] = 0
                    else:    
                        spielplan()



            elif eintragen == 7:
                if 3 in counts or 4 in counts or 5 in counts:
                    plan[eintragen] = sum(wuerfel)
                    counter[eintragen] = sum(wuerfel)
                else:
                    print 'Das ist kein dreier Pasch'
                    print ''
                    ask=raw_input('Null Punkte eintragen j = ja / n = nein ')
                    if ask == 'j':
                        plan[7] = 'gestrichen / 0'
                        counter[7] = 0
                    else:    
                        spielplan()

            elif eintragen == 8:
                if 4 in counts or 5 in counts:
                    plan[eintragen] = sum(wuerfel)
                    counter[eintragen] = sum(wuerfel)
                else:
                    print 'Das ist kein vierer Pasch'
                    print ''
                    ask=raw_input('Null Punkte eintragen j = ja / n = nein ')
                    if ask == 'j':
                        plan[8] = 'gestrichen / 0'
                        counter[8] = 0
                    else:    
                        spielplan()

            elif eintragen == 9:
                if 3 in counts and 2 in counts:
                    plan[9] = 25
                    counter[9] = 25
                else:
                    print 'Das ist kein Full House'
                    print ''
                    ask=raw_input('Null Punkte eintragen j = ja / n = nein ')
                    if ask == 'j':
                        plan[9] = 'gestrichen / 0'
                        counter[9] = 0
                    else:    
                        spielplan()
                    
            elif eintragen == 10:
                if wuerfelNeu[-2] == wuerfelNeu[-1] -1 and wuerfelNeu[-3] == wuerfelNeu[-2] - 1 and wuerfelNeu[-4] == wuerfelNeu[-3] - 1:
                    plan[10] = 30
                    counter[10] = 30
                else:
                    print 'Das ist keine kleine Straße'
                    print ''
                    ask=raw_input('Null Punkte eintragen j = ja / n = nein ')
                    if ask == 'j':
                        plan[10] = 'gestrichen / 0'
                        counter[10] = 0
                    else:    
                        spielplan()

            elif eintragen == 11:
                if wuerfelNeu[-2] == wuerfelNeu[-1] - 1 and wuerfelNeu[-3] == wuerfelNeu[-2] - 1 and wuerfelNeu[-4] == wuerfelNeu[-3] - 1 and wuerfelNeu[-5] == wuerfelNeu[-4] - 1:
                    plan[11] = 40
                    counter[11] = 40
                else:
                    print 'Das ist keine große Straße'
                    print ''
                    ask=raw_input('Null Punkte eintragen j = ja / n = nein ')
                    if ask == 'j':
                        plan[11] = 'gestrichen / 0'
                        counter[11] = 0
                    else:    
                        spielplan()

            elif eintragen == 12:
                if 5 in counts:
                    plan[12] = 50
                    counter[12] = 50
                else:
                    print 'Das ist kein Kniffel'
                    print ''
                    ask=raw_input('Null Punkte eintragen j = ja / n = nein ')
                    if ask == 'j':
                        plan[12] = 'gestrichen / 0'
                        counter[12] = 0
                    else:    
                        spielplan()

            elif eintragen == 13:
                plan[13] = sum(wuerfel)
                counter[13] = sum(wuerfel)


        else:
            print 'Dieses Feld ist schon ausgefüllt'
            wuerfelZeigen()
            spielplan()

        
    def wuerfelZeigen():
        reihe=1
        print ''
        for i in wuerfel:   # Schleife um den Entwert der Wuerfel anzuzeigen
            print 'Würfel', reihe, ':  ', i
            reihe+=1
        print ''
        

    def wurf2_3():
        try:
            for j in range(5):
                inp = raw_input(welcheWuerfel)
                if inp=='w':
                    break
                else:
                    inp = int(inp)-1
                    wuerfel[int(inp)] = random.randint(1, 6)
            wuerfelZeigen()
        except:
            print fehler
            wurf2_3()


    for i in range(rundenzahl):
        planZeigen()
        punkte()
        print ''
        print '##############################################################################'
        print '#################################  Runde:', runde,' #################################'
        print '##############################################################################'
        print ''

        runde+=1

        for i in range(5):   # Schleife fuer den ersten Wurf
            wuerfel[i] = random.randint(1, 6)

        wuerfelZeigen()
        print erklaerung
        print ''
        print '########## Erstes mal würfeln ##########'
        print ''
        wurf2_3()
        print '########## Zweites mal würfeln ##########'
        print ''
        wurf2_3()
        print ''
        spielplan()
        punkte()
    print '##### Spiel Ende #####'
    print ''
    planZeigen()
    punkte()
except:
   print 'Es ist ein unerwarteter Fehler aufgetreten.'
